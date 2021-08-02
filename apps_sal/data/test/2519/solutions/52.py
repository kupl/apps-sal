N, K = list(map(int, input().split()))
lst = list(map(int, input().split()))

n = sum(lst[:K])
m = n

for i in range(N - K):
    l = lst[i]
    r = lst[i + K]
    n = n + r - l

    if m < n:
        m = n

ans = (m + K) / 2
print(ans)
