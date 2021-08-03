import math


def factorization(n):
    arr = [1]
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append(i)

    if temp != 1:
        arr.append(temp)

    if not arr:
        arr.append(n)

    return arr


A, B = list(map(int, input().split()))

gcd = math.gcd(A, B)
f = factorization(gcd)
print((len(f)))
