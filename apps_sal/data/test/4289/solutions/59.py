import numpy as np
n = int(input())
(t, a) = map(int, input().split())
li = list(map(int, input().split()))
t = t * 1000
a = a * 1000
npli = np.array(li)
npli = t - npli * 6
res = npli[0]
res_num = 1
for i in range(n):
    if abs(a - res) > abs(a - npli[i]):
        res = npli[i]
        res_num = i + 1
print(res_num)
