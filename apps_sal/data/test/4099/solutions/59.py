(n, k, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
if m * n - sum(a) > k:
    print(-1)
else:
    print(max(m * n - sum(a), 0))
