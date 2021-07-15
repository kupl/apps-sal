import bisect
n = int(input())
L = sorted(map(int, input().split()))
m = L[-1]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        k = L[i] + L[j]
        ans += bisect.bisect_left(L, k) - j-1
print(ans)

