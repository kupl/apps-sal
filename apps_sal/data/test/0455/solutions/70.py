import sys

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

mod = sum(XY[0]) % 2
if any(mod != ((x + y) % 2) for x, y in XY):
    print(-1)
    return

m = 33 - mod
print(m)
D = [2 ** i for i in range(31, -1, -1)]
if mod == 0:
    D.append(1)

print(' '.join(map(str, D)))
for x, y in XY:
    w = ''
    for d in D:
        if 0 <= x - y and 0 <= x + y:
            w += 'R'
            x -= d
        elif 0 > x - y and 0 <= x + y:
            w += 'U'
            y -= d
        elif 0 <= x - y and 0 > x + y:
            w += 'D'
            y += d
        else:
            w += 'L'
            x += d
    print(w)
