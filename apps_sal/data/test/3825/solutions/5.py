import itertools
STC = [[0, 4, 0, 5], [1, 0, 8, 0], [1, 0, 0, 5]]


def ch(N, K):
    ans = 1
    for k in range(K):
        ans *= N - k
    for k in range(K):
        ans //= k + 1
    return ans


N = int(input())
ans = ch(N + 3, 3)
sgn = -1
for s in range(1, len(STC) + 1):
    for cb in itertools.combinations(STC, s):
        aq = [0, 0, 0, 0]
        for c in cb:
            for i in range(4):
                aq[i] = max(aq[i], c[i])
        tot = sum(aq)
        if N >= tot:
            ans += sgn * ch(N - tot + 3, 3)
    sgn *= -1
print(ans)
