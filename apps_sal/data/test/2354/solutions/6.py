N, Q = map(int, input().split())
qs = [tuple(map(lambda x:int(x) - 1, input().split())) for i in range(Q)]

M = (N * N + 1) // 2

ans = []
if N % 2:
    for y, x in qs:
        a = 1
        if (x + y) % 2:
            a += M
        a += x // 2
        a += N * (y // 2)
        if y % 2:
            if (x + y) % 2:
                a += N // 2
            else:
                a += N // 2 + 1
        ans.append(a)
else:
    for y, x in qs:
        a = 1
        if (x + y) % 2:
            a += M
        a += x // 2
        a += N // 2 * y
        ans.append(a)
print(*ans, sep='\n')
