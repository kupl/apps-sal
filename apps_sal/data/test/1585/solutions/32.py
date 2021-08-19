(x, y) = map(int, input().split())
c = 0
while x <= y:
    c += 1
    x = x * 2
print(c)
