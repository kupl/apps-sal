y, b, r = map(int, input().split())
res = 6
y -= 1
b -= 2
r -= 3
while y * b * r:
    res += 3
    y -= 1
    b -= 1
    r -= 1
print(res)
