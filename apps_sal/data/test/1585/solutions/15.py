(x, y) = map(int, input().split())
n = 0
v = x
while v <= y:
    n += 1
    v *= 2
print(n)
