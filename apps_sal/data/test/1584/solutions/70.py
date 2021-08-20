import bisect
N = int(input())
L = list(map(int, input().split()))
L = sorted(L)
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        ind = bisect.bisect_left(L, L[i] + L[j])
        num = ind - (j + 1)
        ans += max(num, 0)
print(ans)
