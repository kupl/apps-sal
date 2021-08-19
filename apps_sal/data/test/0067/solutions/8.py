(x, y, z) = map(int, input().split())
res = '?'
if x < y:
    if x + z < y:
        res = '-'
elif y < x:
    if y + z < x:
        res = '+'
elif x == y and z == 0:
    res = '0'
print(res)
