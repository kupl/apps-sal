import math
n = int(input())


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


f = factorization(n)
l = len(f)
x = 0
for i in range(l):
    x += int((-1 + math.sqrt(1 + 8 * f[i][1])) // 2)
if n == 1:
    x = 0
print(x)
