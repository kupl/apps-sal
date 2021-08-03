def sgn(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1


n = int(input())
x = 0
y = 0
res = 0
last = 0
for ch in input().strip():
    if ch == 'U':
        y += 1
    else:
        x += 1
    if sgn(x - y) * last < 0:
        res += 1
    if x != y:
        last = sgn(x - y)

print(res)
