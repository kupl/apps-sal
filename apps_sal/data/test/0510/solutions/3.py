a, b, c, d = list(map(int, input().split()))
p = sorted([a, b, c])
print(max(0, d - (p[1] - p[0])) + max(0, d - (p[2] - p[1])))
