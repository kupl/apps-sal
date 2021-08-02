import math
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

remain_p = sorted(p)
remain_q = sorted(q)
a = 0
b = 0
for i in range(n):
    a += math.factorial(n - (i + 1)) * (remain_p.index(p[i]) + 1) - 1
    b += math.factorial(n - (i + 1)) * (remain_q.index(q[i]) + 1) - 1
    remain_p.remove(p[i])
    remain_q.remove(q[i])

ans = a - b
if ans >= 0:
    print(ans)
else:
    print((-ans))
