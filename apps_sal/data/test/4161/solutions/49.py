K = int(input())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


result = 0

for a in range(1, K + 1):
    result += a
    b = a + 1
    while b <= K:
        result += 6 * gcd(a, b)
        l = gcd(a, b)
        c = b + 1
        while c <= K:
            result += 6 * gcd(l, c)
            c += 1
        b += 1
print(result)
