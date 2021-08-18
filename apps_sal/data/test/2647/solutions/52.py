from collections import deque
import copy
H, W = map(int, input().split())
s = [list(input()) for i in range(H)]

ss = copy.deepcopy(s)
q = deque([[0, 0]])
ss[0][0] = 0
move = [[1, 0], [0, 1], [0, -1], [-1, 0]]
num = 0
t = False
while q:
    num += 1
    for i in range(len(q)):
        b = q.popleft()
        if b == [H - 1, W - 1]:
            t = True
            num -= 1
            break
        for m in move:
            if 0 <= b[0] + m[0] <= H - 1 and 0 <= b[1] + m[1] <= W - 1 and ss[b[0] + m[0]][b[1] + m[1]] == '.':
                ss[b[0] + m[0]][b[1] + m[1]] = num
                q.append([b[0] + m[0], b[1] + m[1]])
    else:
        continue
    break
if not t:
    print('-1')
else:
    x = num
    b = H - 1, W - 1
    ss[b[0]][b[1]] = '
    while x != 0:
        for m in move:
            if 0 <= b[0] + m[0] <= H - 1 and 0 <= b[1] + m[1] <= W - 1 and ss[b[0] + m[0]][b[1] + m[1]] == x - 1:
                x = x - 1
                ss[b[0] + m[0]][b[1] + m[1]] = '
                b = b[0] + m[0], b[1] + m[1]
                break
    ans = 0
    for h in range(H):
        for w in range(W):
            if ss[h][w] != '
            ans += 1
    print(ans)
