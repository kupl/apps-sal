from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))
L = sorted(L)
ans = 0

for i in range(N - 2):
    a = L[i]
    for j in range(i + 1, N - 1):
        b = L[j]
        ans += bisect_left(L, a + b) - (j + 1)
print(ans)
