def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


(n, k) = map(int, input().split())
n1 = n
k1 = k
a = n1 // gcd(n, 10 ** k) * 10 ** k1
print(a)
