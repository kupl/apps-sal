mod = 1000000000 + 7


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
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


n = int(input())
dat = [0] * 2000
res = 1
for i in range(1, n + 1):
    d = factorization(i)
    for j in range(len(d)):
        dat[d[j][0]] += d[j][1]
for i in range(2, n + 1):
    res *= dat[i] + 1
    res %= mod
print(res)
