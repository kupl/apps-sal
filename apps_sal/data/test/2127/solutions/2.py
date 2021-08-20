T = int(input())
x = 0
y = 0
uu = []
for _ in range(T):
    (p, a, b) = input().split()
    a = int(a)
    b = int(b)
    if p == '+':
        x = max(x, max(a, b))
        y = max(y, min(a, b))
    elif max(a, b) >= x and min(a, b) >= y:
        uu.append('YES')
    else:
        uu.append('NO')
print('\n'.join(uu))
