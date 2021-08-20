(x, y) = map(int, input().split())
res = 0
while x <= y:
    x *= 2
    res += 1
print(res)
