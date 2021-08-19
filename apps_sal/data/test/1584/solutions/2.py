import bisect
N = int(input())
L = list(map(int, input().split()))
ans = 0
L.sort()
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        num = L[i] + L[j]
        ind = bisect.bisect_right(L, num - 1)
        if ind > j - 1:
            ans += ind - j - 1
print(ans)
