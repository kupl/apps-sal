(n, m) = map(int, input().split())
t = list(((i - 1) // m for i in map(int, input().split())))
t.reverse()
print(n - t.index(max(t)))
