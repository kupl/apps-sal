n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
def f(a, b, c): return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def g(fi, se, p):
    q = []
    for x in p:
        if f(fi, se, x):
            if len(q) < 2:
                q.append(x)
            else:
                if f(q[0], q[1], x):
                    return 1
    return 0


print('NO' if n > 4 and all([g(p[0], p[1], p), g(p[0], p[2], p), g(p[1], p[2], p)]) else 'YES')
