from bisect import bisect_left


N, *L = list(map(int, open(0).read().split()))
L.sort()

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        a = L[i]
        b = L[j]
        ans += bisect_left(L, a + b, lo=j + 1) - (j + 1)
print(ans)
