
n = int(input())
p = list(map(int, input().split()))

r = list(range(n))
l = list(range(n))
I = [-1] * (n + 1)

for i, P in enumerate(p):
    I[P] = i
ans = 0

for N, index in enumerate(I[1:], 1):
    L = index - 1
    if L >= 0:
        L = l[L]

    R = index + 1
    if R < n:
        R = r[R]

    l[R - 1] = L
    r[L + 1] = R
    if L >= 0:
        L2 = L - 1
        if L2 >= 0:
            L2 = l[L2]
        ans += N * (L - L2) * (R - index)

    if R < n:
        R2 = R + 1
        if R2 < n:
            R2 = r[R2]
        ans += N * (index - L) * (R2 - R)
print(ans)
