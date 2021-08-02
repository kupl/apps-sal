N = int(input())
P = list(map(int, input().split()))
R = list(range(N))
L = list(range(N))
I = [-1] * (N + 1)
for i, p in enumerate(P):
    I[p] = i

ans = 0
for n, idx in enumerate(I[1:], 1):
    l = idx - 1
    if l >= 0:
        l = L[l]
    r = idx + 1
    if r < N:
        r = R[r]
    L[r - 1] = l
    R[l + 1] = r

    if l >= 0:
        l2 = l - 1
        if l2 >= 0:
            l2 = L[l2]
        ans += n * (l - l2) * (r - idx)
    if r < N:
        r2 = r + 1
        if r2 < N:
            r2 = R[r2]
        ans += n * (idx - l) * (r2 - r)
print(ans)
