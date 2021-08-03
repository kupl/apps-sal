a, b = list(map(int, input().split()))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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


t = factorization(gcd(a, b))
if t[0][0] == 1:
    print((1))
    return
print((len(t) + 1))
