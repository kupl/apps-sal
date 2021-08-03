import math
a, b = map(int, input().split())


def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(n**0.5) + 1):
        while tmp % i == 0:
            tmp //= i
            arr.append(i)
    if tmp != 1:
        arr.append(tmp)
    if arr == []:
        arr.append(n)
    return list(set(arr))


ans = len(factorization(math.gcd(a, b)))
print(ans + 1 if math.gcd(a, b) != 1 else 1)
