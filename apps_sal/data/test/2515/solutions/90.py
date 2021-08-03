import itertools
import copy
q = int(input())
qr = [list(map(int, input().split())) for i in range(q)]
sosu = [1] * (10**5 + 1)
sosu[0] = 0
sosu[1] = 0
k = 2
while k < (10**5 + 1)**0.5 + 1:
    for i in range(2 * k, 10**5 + 1, k):
        sosu[i] = 0
    if k == 2:
        k += 1
    else:
        k += 2

n = [0] * (10**5 + 1)
for i in range(1, len(sosu)):
    if i % 2 == 1 and sosu[i] == 1 and sosu[(i + 1) // 2] == 1:
        n[i] = 1
ans = list(itertools.accumulate(n))
for i in range(q):
    print(ans[qr[i][1]] - ans[qr[i][0] - 1])
