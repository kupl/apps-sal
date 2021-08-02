*p, d = list(map(int, input().split()))
p.sort()

r = max(0, d - (p[1] - p[0])) + max(0, d - (p[2] - p[1]))
print(r)
