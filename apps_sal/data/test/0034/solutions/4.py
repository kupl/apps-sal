n, a, b = map(int, input().split())
r = set()
for m in range(1, n):
    r.add(min(a // m, b // (n - m)))
print(max(r))
