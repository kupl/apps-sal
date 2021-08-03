a, b, c, d = map(int, input().split())
print(max([i * j for i in (a, b) for j in (c, d)]))
