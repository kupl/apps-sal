import sys
f = sys.stdin
n = int(f.readline().strip())
fig = []
place = []
for i in range(n):
    place.append([-1] * n)
for i in range(n):
    s = f.readline().strip()
    for k in range(len(s)):
        if s[k] == 'o':
            fig.append((k, i))
            place[k][i] = -1
        elif s[k] == 'x':
            place[k][i] = 1
        elif s[k] == '.':
            place[k][i] = 0
hh = []
for i in range(2 * n - 1):
    hh.append([1] * (2 * n - 1))
res = True
for fi in range(len(fig)):
    x = fig[fi][0]
    y = fig[fi][1]
    for i in range(n):
        for k in range(n):
            r = place[k][i]
            if r == 0:
                dx = k - x + n - 1
                dy = i - y + n - 1
                hh[dx][dy] = 0
for i in range(n):
    for k in range(n):
        r = place[k][i]
        if r == 1:
            beat = False
            for fi in range(len(fig)):
                dx = k - fig[fi][0] + n - 1
                dy = i - fig[fi][1] + n - 1
                if hh[dx][dy] != 0:
                    beat = True
            if not beat:
                res = False
hh[n - 1][n - 1] = -1
if res:
    print('YES')
    for i in range(2 * n - 1):
        s = ''
        for k in range(2 * n - 1):
            if hh[k][i] == 0:
                s += '.'
            elif hh[k][i] == -1:
                s += 'o'
            else:
                s += 'x'
        print(s)
else:
    print('NO')
