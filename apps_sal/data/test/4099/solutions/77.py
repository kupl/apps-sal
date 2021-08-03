n, k, m = map(int, input().split())
a = list(map(int, input().split()))
x = max(0, m * n - sum(a))
print(x if x <= k else -1)
