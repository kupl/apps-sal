(N, X) = map(int, input().split())
siz = [1]
pat = [1]
for i in range(N):
    siz.append(siz[-1] * 2 + 3)
    pat.append(pat[-1] * 2 + 1)


def rec(n, x):
    if n == 0:
        ret = int(x > 0)
    elif x <= 1 + siz[n - 1]:
        ret = rec(n - 1, x - 1)
    else:
        ret = pat[n - 1] + 1 + rec(n - 1, x - 2 - siz[n - 1])
    return ret


print(rec(N, X))
