(A, B, K) = map(int, input().split())


def gcd(a, b):
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a


C = gcd(A, B)
i = C + 1
while K > 0:
    i -= 1
    if C % i == 0:
        K -= 1
print(i)
