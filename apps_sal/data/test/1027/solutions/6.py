from sys import stdin, stdout
from math import factorial
from math import log10
n = 14
challengers = list(map(int, stdin.readline().split()))
ans = 0
for i in range(n):
    if not challengers[i]:
        continue
    test = challengers[:]
    cnt = test[i]
    test[i] = 0
    for j in range(i + 1, n):
        test[j] += 1
        cnt -= 1
        if cnt == 0:
            break
    value = cnt // 14
    for j in range(n):
        test[j] += value
        cnt -= value
    for j in range(cnt % 14):
        test[j] += 1
    cur_ans = 0
    for z in range(n):
        if not test[z] & 1:
            cur_ans += test[z]
    ans = max(ans, cur_ans)
stdout.write(str(ans))
