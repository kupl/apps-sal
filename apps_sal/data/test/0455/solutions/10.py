def solve(n, x, y):
    ws = []
    S = set()
    for i in range(n):
        u = x[i] + y[i]
        v = x[i] - y[i]
        S.add(u % 2)
        if len(S) > 1:
            print(-1)
            return
        ds = [2 ** k for k in range(30, -1, -1)]
        if u % 2 == 0:
            ds.append(1)
        w = ''
        for d in ds:
            if u >= 0 and v >= 0:
                w += 'R'
                (u, v) = (u - d, v - d)
            elif u <= 0 and v <= 0:
                w += 'L'
                (u, v) = (u + d, v + d)
            elif u >= 0 and v <= 0:
                w += 'U'
                (u, v) = (u - d, v + d)
            else:
                w += 'D'
                (u, v) = (u + d, v - d)
        ws.append(w)
    print(len(ds))
    print(' '.join(map(str, ds)))
    print('\n'.join(ws))


n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    (x[i], y[i]) = map(int, input().split())
solve(n, x, y)
