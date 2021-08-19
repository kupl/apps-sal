""" بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ """


def gi():
    return list(map(int, input().split()))


(n,) = gi()
g = [list(map(int, list(input()))) for _ in range(n)]
(lenp,) = gi()
p = gi()
ans = p[:]
lenans = lenp
k = 1
while k < lenp - 1:
    if g[ans[k - 1] - 1][ans[k + 1] - 1] == 0 and ans[k - 1] != ans[k + 1]:
        p[k] = -1
        ans[k] = ans[k - 1]
        lenans -= 1
        k += 1
    k += 1
print(lenans)
for k in range(lenp):
    if p[k] != -1:
        print(ans[k], end=' ')
