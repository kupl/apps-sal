from collections import Counter
from itertools import permutations
(n, c) = list(map(int, input().split()))
D = []
for i in range(c):
    D.append(list(map(int, input().split())))
co = [Counter() for i in range(3)]
for i in range(n):
    C = list(map(int, input().split()))
    for j in range(n):
        co[(i + j) % 3][C[j] - 1] += 1
ans = 10 ** 15
perm = permutations([i for i in range(c)], 3)
for t in perm:
    temp = 0
    for i in range(3):
        color = t[i]
        for (num, cnt) in list(co[i].items()):
            temp += D[num][color] * cnt
    ans = min(temp, ans)
print(ans)
