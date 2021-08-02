import sys

N = int(input())
coord = [tuple(map(int, input().split())) for _ in range(N)]
parity = (coord[0][0] + coord[0][1]) % 2
flag = False
for c in coord[1:]:
    if (c[0] + c[1]) % 2 != parity:
        flag = True
        break
if flag:
    print(-1)
    return
D = [2**(31 - i) for i in range(32)]
if parity == 0:
    D.append(1)
print(len(D))
print(*D, sep=' ')
for c in coord:
    w = ''
    pos = [0, 0]
    for d in D:
        dif = [c[0] - pos[0], c[1] - pos[1]]
        cands = [(abs(dif[0] - d) + abs(dif[1]), 'R'), (abs(dif[0] + d) + abs(dif[1]), 'L'), (abs(dif[0]) + abs(dif[1] - d), 'U'), (abs(dif[0]) + abs(dif[1] + d), 'D')]
        select = min(cands)
        w += select[1]
        if select[1] == 'R':
            pos[0] += d
        elif select[1] == 'L':
            pos[0] -= d
        elif select[1] == 'U':
            pos[1] += d
        else:
            pos[1] -= d
    print(w)
