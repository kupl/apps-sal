import sys
sys.setrecursionlimit(10**9)

INF = 10**12
LIM = 20
N = int(input())
D = dict()
for _ in range(N):
    s, c = input().split()
    if s in list(D.keys()):
        D[s] = min(D[s], int(c))
    else:
        D[s] = int(c)


def check_kaibun(s):
    n = len(s)
    return all(s[i] == s[-i - 1] for i in range(n // 2))


def calc_cost(use):
    return sum(D[s] * n for (s, n) in list(use.items()))


def find_candidate(cost, use, s, is_left):
    if check_kaibun(s):
        return min(cost, calc_cost(use))

    if is_left:
        for t in list(D.keys()):
            # reversed s is included in the end of t
            if t[::-1].find(s) == 0:
                use[t] += 1
                if use[t] > LIM:
                    return INF
                c = find_candidate(cost, use, t[:-len(s):], False)
                cost = min(cost, c)
                use[t] -= 1
            # reveresed t is included in the begin of s
            elif s.find(t[::-1]) == 0:
                use[t] += 1
                c = find_candidate(cost, use, s[len(t):], True)
                cost = min(cost, c)
                use[t] -= 1
    else:
        for t in list(D.keys()):
            # t is included in the end of reversed s
            if s[::-1].find(t) == 0:
                use[t] += 1
                c = find_candidate(cost, use, s[:-len(t):], False)
                cost = min(cost, c)
                use[t] -= 1
            # s is included in the begin of reveresed t
            elif t.find(s[::-1]) == 0:
                use[t] += 1
                c = find_candidate(cost, use, t[len(s):], True)
                cost = min(cost, c)
                use[t] -= 1

    return min(cost, INF)


def solve():
    ans = INF
    for s in list(D.keys()):
        use = {s: 0 for s in list(D.keys())}
        use[s] = 1
        ans = find_candidate(ans, use, s, True)
    return ans if ans < INF else -1


def __starting_point():
    print((solve()))


__starting_point()
