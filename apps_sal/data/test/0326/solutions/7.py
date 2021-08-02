def it(): return list(map(int, input().strip().split()))


INF = float('inf')


def solve():
    N = int(input())
    S = []
    C = []
    for _ in range(N):
        s, c = input().strip().split()
        S.append(s)
        C.append(int(c))

    vis = set()
    mem = dict()

    def dp(s, p):
        if (s, p) in mem:
            return mem[s, p]

        if s == s[::-1]:
            return 0

        if (s, p) in vis:
            return INF

        vis.add((s, p))

        ans = INF
        if p == 0:
            for i in range(N):
                if len(S[i]) >= len(s):
                    if S[i][::-1].startswith(s):
                        ans = min(ans, dp(S[i][:-len(s)], 1) + C[i])
                else:
                    if s.startswith(S[i][::-1]):
                        ans = min(ans, dp(s[len(S[i]):], 0) + C[i])
        else:
            for i in range(N):
                if len(S[i]) >= len(s):
                    if S[i].startswith(s[::-1]):
                        ans = min(ans, dp(S[i][len(s):], 0) + C[i])
                else:
                    if s[::-1].startswith(S[i]):
                        ans = min(ans, dp(s[:-len(S[i])], 1) + C[i])

        vis.discard((s, p))
        mem[s, p] = ans
        return ans

    ans = INF
    for i in range(N):
        ans = min(ans, dp(S[i], 0) + C[i])
    return -1 if ans == INF else ans


def __starting_point():
    ans = solve()
    print(ans)


__starting_point()
