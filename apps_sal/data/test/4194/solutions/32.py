(n, m) = map(int, input().split())
a = [int(s) for s in input().split()]
days = n - sum(a)
print(days) if days >= 0 else print(-1)
