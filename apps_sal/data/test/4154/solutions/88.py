n, m = map(int, input().split())
lower = -float('inf')
upper = float('inf')
for i in range(m):
    l, r = map(int, input().split())
    if l > lower:
        lower = l
    if r < upper:
        upper = r
    if upper < lower:
        upper = 0
        lower = 0
        break
if upper == lower == 0:
    print(0)
else:
    print(upper - lower + 1)
