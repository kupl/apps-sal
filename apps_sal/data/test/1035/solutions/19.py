import math


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(pow(n, 1 / 2)) + 1):
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


A, B = map(int, input().split())
gcd_num = math.gcd(A, B)

if gcd_num == 1:
    print(1)
else:
    print(len(factorization(gcd_num)) + 1)
