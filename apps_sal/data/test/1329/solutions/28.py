from collections import defaultdict
n = int(input())


# 素因数分解
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


# factorization(24)
## [[2, 3], [3, 1]]
# 24 = 2^3 * 3^1
d = defaultdict(int)

for i in range(1, n + 1):
    x = factorization(i)
    for xi in x:
        d[xi[0]] += xi[1]
di = defaultdict(int)
for k in d:
    if d[k] >= 74:
        di[74] += 1
        di[24] += 1
        di[14] += 1
        di[4] += 1
        di[2] += 1
    elif d[k] >= 24:
        di[24] += 1
        di[14] += 1
        di[4] += 1
        di[2] += 1
    elif d[k] >= 14:
        di[14] += 1
        di[4] += 1
        di[2] += 1
    elif d[k] >= 4:
        di[4] += 1
        di[2] += 1
    elif d[k] >= 2:
        di[2] += 1
ans = di[74]
ans += max(0, di[24] * (di[2] - 1))
ans += max(0, di[14] * (di[4] - 1))
ans += max(0, (di[4] * (di[4] - 1)) // 2 * (di[2] - 2))
print((max(ans, 0)))
