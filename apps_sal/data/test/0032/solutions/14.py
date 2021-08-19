def solve():
    n = int(input())
    y = 20000
    for i in range(n):
        (l, d) = input().split()
        if y == 20000 and d != 'South':
            return False
        if y == 0 and d != 'North':
            return False
        l = int(l)
        if d == 'South':
            y -= l
        elif d == 'North':
            y += l
        if not 0 <= y <= 20000:
            return False
    return y == 20000


print('YES' if solve() else 'NO')
