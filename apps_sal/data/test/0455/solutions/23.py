n = int(input())
xys = [list(map(int, input().split())) for _ in range(n)]

# 各クエリのパリティをチェックする
p = sum(xys[0]) % 2
for xy in xys:
    x, y = xy
    if (x + y) % 2 != p:  # パリティが異なるクエリが存在するため、達成できない
        print(-1)
        return

if p == 0:
    d = [1]
else:
    d = []

d += [2 ** k for k in range(30 + 1)]  # 2 ** 0 から 2 ** 30 まで
m = len(d)

ws = [['' for _ in range(m)] for _ in range(n)]
idx = 0
for xy in xys:
    x, y = xy
    for k in sorted(range(m), reverse=True):
        R = abs(x - d[k]) + abs(y)
        L = abs(x + d[k]) + abs(y)
        U = abs(x) + abs(y - d[k])
        D = abs(x) + abs(y + d[k])

        min_v = min(R, L, U, D)

        if min_v == R:
            ws[idx][k] = 'R'
            x -= d[k]
        elif min_v == L:
            ws[idx][k] = 'L'
            x += d[k]
        elif min_v == U:
            ws[idx][k] = 'U'
            y -= d[k]
        else:
            # if min_v == D:
            ws[idx][k] = 'D'
            y += d[k]
    idx += 1

print(m)
print(*d)
for w in ws:
    print(''.join(w))
