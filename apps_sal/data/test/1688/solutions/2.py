import bisect
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

B = [(-a, i) for i, a in enumerate(A)]


LIST = deque()
LIST.append(B[0])

for b, i in B[1:]:
    if b > LIST[-1][0]:
        LIST.append((b, i))


DIS = [-1] * n

for i in range(n - 1, -1, -1):
    x = bisect.bisect(LIST, (-A[i] // 2, 1 << 20))
    if x < len(LIST):
        DIS[i] = LIST[x][1]

    while len(LIST) >= 1 and A[i] <= -LIST[0][0]:
        LIST.popleft()

    LIST.appendleft(B[i])

if max(DIS) == -1:
    print(*[-1] * n)
    return

for i in range(n):
    if DIS[i] != -1:
        start = i
        break

ANS = [-1] * n

if DIS[start] > start:
    ANS[start] = DIS[start] - start
else:
    ANS[start] = DIS[start] + (n - start)


for i in range(start - 1, -1, -1):
    if DIS[i] == -1:
        ANS[i] = ANS[(i + 1) % n] + 1
    else:
        if DIS[i] > i:
            ANS[i] = min(DIS[i] - i, ANS[(i + 1) % n] + 1)
        else:
            ANS[i] = min(DIS[i] + (n - i), ANS[(i + 1) % n] + 1)

for i in range(n - 1, -1, -1):
    if DIS[i] == -1:
        ANS[i] = ANS[(i + 1) % n] + 1
    else:
        if DIS[i] > i:
            ANS[i] = min(DIS[i] - i, ANS[(i + 1) % n] + 1)
        else:
            ANS[i] = min(DIS[i] + (n - i), ANS[(i + 1) % n] + 1)

for i in range(n - 1, -1, -1):
    if DIS[i] == -1:
        ANS[i] = ANS[(i + 1) % n] + 1
    else:
        if DIS[i] > i:
            ANS[i] = min(DIS[i] - i, ANS[(i + 1) % n] + 1)
        else:
            ANS[i] = min(DIS[i] + (n - i), ANS[(i + 1) % n] + 1)


print(*ANS)
