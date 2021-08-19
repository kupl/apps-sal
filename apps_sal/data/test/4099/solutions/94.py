(n, k, m) = map(int, input().split())
a = list(map(int, input().split()))
need = m * n - sum(a)
print(0 if need < 0 else need if need <= k else -1)
