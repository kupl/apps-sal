N = int(input())

point = []
parity = {}
for _ in range(N):
    x, y = list(map(int, input().split()))
    point.append((x, y))
    parity[(x + y) % 2] = 1

if len(set(parity)) == 2:
    print('-1')
else:
    m = 38
    parity = 1 if (1 in parity) else 0
    print((m + 1 - parity))
    if parity == 1:  # 距離が奇数
        print((*[1 << i for i in range(m)]))
    else:
        print((1, *[1 << i for i in range(m)]))

    def arm(x, y, m):
        if abs(x) >= abs(y):
            if x >= 0:
                return ('R', x - (1 << m), y)
            else:
                return ('L', x + (1 << m), y)
        else:
            if y >= 0:
                return ('U', x, y - (1 << m))
            else:
                return ('D', x, y + (1 << m))

    for x, y in point:
        ans = []
        for i in range(m - 1, -1, -1):
            mode, x, y = arm(x, y, i)
            ans.append(mode)
        if parity == 0:  # 偶数の場合一つ足す
            if x == 1:
                ans.append('R')
            elif x == -1:
                ans.append('L')
            elif y == 1:
                ans.append('U')
            elif y == -1:
                ans.append('D')
        print((''.join(ans[::-1])))
