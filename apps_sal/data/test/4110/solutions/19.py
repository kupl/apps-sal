from itertools import product
import math
(D, G) = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]
ans = []
for lst in product([0, 1], repeat=D):
    temp = 0
    cnt = 0
    max0 = -1
    p = 0
    for (i, j) in enumerate(lst):
        temp += (pc[i][0] * 100 * (i + 1) + pc[i][1]) * j
        cnt += pc[i][0] * j
        if j == 0 and max0 < i:
            max0 = i
    if temp < G and max0 != -1:
        p = math.ceil((G - temp) / (100 * (max0 + 1)))
        if p < pc[max0][0]:
            cnt += p
            temp += p * 100 * (max0 + 1)
    if temp >= G:
        ans.append(cnt)
print(min(ans))
