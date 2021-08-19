(a, b) = map(int, input().split())
c = b - a
res = sum((i for i in range(c)))
print(res - a)
