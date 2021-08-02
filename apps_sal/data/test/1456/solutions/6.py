n = int(input())
b = [input() for i in range(n)]
h = [[False] * n for i in range(n)]
p = [[i, j] for i in range(n) for j in range(n) if b[i][j] == 'o']
v = [['.'] * (2 * n - 1) for i in range(2 * n - 1)]


def on(x, y):
    return x in range(n) and y in range(n)


def proc(dx, dy):
    for pi in p:
        if on(pi[0] + dx, pi[1] + dy) and b[pi[0] + dx][pi[1] + dy] == '.':
            return
    v[dx + n - 1][dy + n - 1] = 'x'
    for pi in p:
        if on(pi[0] + dx, pi[1] + dy):
            h[pi[0] + dx][pi[1] + dy] = True


for i in range(-(n - 1), n):
    for j in range(-(n - 1), n):
        proc(i, j)
if any(b[i][j] == 'x' and not h[i][j] for i in range(n) for j in range(n)):
    print('NO')
else:
    print('YES')
    v[n - 1][n - 1] = 'o'
    for vi in v:
        print(''.join(vi))
