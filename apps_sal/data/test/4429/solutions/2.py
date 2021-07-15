def solve():
    x, y, z = map(int, input().split())
    for s in range(1 << 3):
        a = x if s & 1 else y
        b = x if s & 2 else z
        c = y if s & 4 else z
        if x == max(a, b) and y == max(a, c) and z == max(b, c):
            print('YES')
            print(a, b, c)
            return
    print('NO')

t = int(input())
for _ in range(t):
    solve()
