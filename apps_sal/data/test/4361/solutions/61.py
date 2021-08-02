N, K = list(map(int, input().split()))
a = [int(input()) for i in range(N)]

a.sort()
ans = 100000000000000000000000

for j in range(N - K + 1):
    if a[j + K - 1] - a[j] < ans:
        ans = a[j + K - 1] - a[j]


print(ans)
