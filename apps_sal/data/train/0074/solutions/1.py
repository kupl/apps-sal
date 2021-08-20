from operator import itemgetter
import sys


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


def main():
    inf = 10 ** 9
    for _ in range(II()):
        (n, k) = MI()
        ab = [(a, b, i) for (i, (a, b)) in enumerate(LLI(n))]
        dp = [[inf] * n for _ in range(k)]
        log = [[[] for _ in range(n)] for _ in range(k)]
        for e in range(n):
            dp[0][e] = -ab[e][0]
        ab.sort(key=itemgetter(1))
        for (a, b, i) in ab:
            for j in range(k - 2, -1, -1):
                for e in range(n):
                    if i == e:
                        continue
                    pre = dp[j][e]
                    if pre == inf:
                        continue
                    cur = pre + b * (k - 1 - j) - a
                    if cur < dp[j + 1][e]:
                        dp[j + 1][e] = cur
                        log[j + 1][e] = log[j][e] + [i]
        mn = mne = inf
        for e in range(n):
            cur = dp[-1][e]
            if cur < mn:
                mn = cur
                mne = e
        first = log[-1][mne]
        use = [False] * n
        use[mne] = True
        ans = []
        for i in first:
            ans.append(i + 1)
            use[i] = True
        for i in range(n):
            if use[i]:
                continue
            ans.append(i + 1)
            ans.append(-i - 1)
        ans.append(mne + 1)
        print(len(ans))
        print(*ans)


main()
