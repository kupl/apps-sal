(a, b) = map(int, input().split())
c = str(a) * b
d = str(b) * a
print(min(c, d))
