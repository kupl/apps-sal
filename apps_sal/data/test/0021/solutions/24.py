n = int(input())
a = list(map(int, input().split()))
p1 = a.index(1)
p2 = a.index(n)
op = min(p1 - 0, n - p1 - 1, p2 - 0, n - p2 - 1)
print(n - op - 1)
