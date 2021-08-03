import numpy as np
N = int(input())
dp = [0] * (N + 1)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


for i in range(1, N + 1):
    p = factorization(i)
    for x, y in p:
        dp[x] += y
nplist = np.array(dp)
a = nplist[nplist >= 2]
b = nplist[nplist >= 4]
c = nplist[nplist >= 14]
d = nplist[nplist >= 24]
e = nplist[nplist >= 74]
f = len(e)
g = len(d) * (len(a) - 1)
h = len(c) * (len(b) - 1)
k = len(b) * (len(b) - 1) * (len(a) - 2) // 2
print(f + g + h + k)
