from collections import defaultdict
import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    n = int(input())
    S = input().strip()
    ANS = 1 << 31
    D = defaultdict(list)
    NOW = [0, 0]
    TIME = 0
    D[tuple(NOW)].append(TIME)
    TIME += 1
    for s in S:
        if s == 'U':
            NOW[0] += 1
        elif s == 'D':
            NOW[0] -= 1
        elif s == 'R':
            NOW[1] += 1
        else:
            NOW[1] -= 1
        D[tuple(NOW)].append(TIME)
        TIME += 1
        if len(D[tuple(NOW)]) > 1 and ANS > D[tuple(NOW)][-1] - D[tuple(NOW)][-2]:
            ANS = D[tuple(NOW)][-1] - D[tuple(NOW)][-2]
            ANSX = (D[tuple(NOW)][-2] + 1, D[tuple(NOW)][-1])
    if ANS == 1 << 31:
        print(-1)
    else:
        print(*ANSX)
