def mp():
    return map(int, input().split())


t = int(input())
for tt in range(t):
    x, y = mp()
    if x - y == 1:
        print('NO')
    else:
        print('YES')
