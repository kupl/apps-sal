from collections import deque
import math

import sys
input = sys.stdin.readline

N, D, A = list(map(int, input().split()))
S = [0] * N
atack = deque()
for i in range(N):
    x, h = list(map(int, input().split()))
    S[i] = [x, h]

S.sort()
cnt = 0
dmg = 0
for i in range(N):
    while atack:
        if atack[0][0] < S[i][0]:
            x, d = atack.popleft()
            dmg -= d
        else:
            break

    if S[i][1] <= dmg:
        continue
    bomb = math.ceil((S[i][1] - dmg) / A)
    atack.append([S[i][0] + 2 * D, A * bomb])
    cnt += bomb
    dmg += A * bomb

print(cnt)
