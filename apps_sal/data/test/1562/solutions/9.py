import math
n, m, k, q = list(map(int, input().split()))
right = [-1] * n
left = [-1] * n
for i in range(k):
    row, col = list(map(int, input().split()))
    row -= 1
    col -= 1
    if right[row] == -1:
        right[row] = left[row] = col
    else:
        right[row] = max(right[row], col)
        left[row] = min(left[row], col)
safe = sorted(list([int(qi) - 1 for qi in input().split()]))
lup = [0] * m
rup = [0] * m
j = 0
while j < safe[0]:
    lup[j] = -1
    rup[j] = safe[0]
    j += 1
lup[j] = rup[j] = safe[0]
for i in range(1, q):
    j = safe[i - 1]
    while j < safe[i]:
        lup[j] = safe[i - 1]
        rup[j] = safe[i]
        j += 1
j = safe[-1]
while j < m:
    lup[j] = safe[-1]
    rup[j] = -1
    j += 1
if left[0] == -1:
    left[0] = right[0] = 0
dleft = right[0] + (right[0] - left[0])
dright = right[0]
lastn = 0
for i in range(1, n):
    if left[i] == -1:
        continue
    left_1b = lup[left[lastn]]
    left_2b = rup[left[lastn]]
    right_1b = lup[right[lastn]]
    right_2b = rup[right[lastn]]
    ilen = right[i] - left[i]
    ll1: int
    ll2: int
    rl1: int
    rl2: int
    if left_1b != -1:
        ll1 = (left[lastn] - left_1b) + abs(right[i] - left_1b)
    else:
        ll1 = math.inf
    if left_2b != -1:
        ll2 = (left_2b - left[lastn]) + abs(right[i] - left_2b)
    else:
        ll2 = math.inf
    if right_1b != -1:
        rl1 = (right[lastn] - right_1b) + abs(right[i] - right_1b)
    else:
        rl1 = math.inf
    if right_2b != -1:
        rl2 = (right_2b - right[lastn]) + abs(right[i] - right_2b)
    else:
        rl2 = math.inf
    dleft_new = min(dleft + min(ll1, ll2), dright + min(rl1, rl2)) + ilen
    lr1: int
    lr2: int
    rr1: int
    rr2: int
    if left_1b != -1:
        lr1 = (left[lastn] - left_1b) + abs(left[i] - left_1b)
    else:
        lr1 = math.inf
    if left_2b != -1:
        lr2 = (left_2b - left[lastn]) + abs(left[i] - left_2b)
    else:
        lr2 = math.inf
    if right_1b != -1:
        rr1 = (right[lastn] - right_1b) + abs(left[i] - right_1b)
    else:
        rr1 = math.inf
    if right_2b != -1:
        rr2 = (right_2b - right[lastn]) + abs(left[i] - right_2b)
    else:
        rr2 = math.inf
    dright_new = min(dleft + min(lr1, lr2), dright + min(rr1, rr2)) + ilen
    dleft, dright = dleft_new, dright_new
    lastn = i
print(min(dleft, dright) + lastn)
