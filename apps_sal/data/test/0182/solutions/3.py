a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
have = 0
if a > x:
    have += (a - x) // 2
if b > y:
    have += (b - y) // 2
if c > z:
    have += (c - z) // 2

need = max(0, x - a) + max(0, y - b) + max(0, z - c)
if have >= need:
    print('Yes')
else:
    print('No')
