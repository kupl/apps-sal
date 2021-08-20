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


N = int(input())
L = factorization(N)
a = 0
for (p, e) in L:
    if p == 1:
        continue
    t = 1
    while t <= e:
        a += 1
        e -= t
        t += 1
print(a)
