def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


(n, k) = map(int, input().split())
l = 1
for i in range(k):
    l *= 10
print(str(n // gcd(n, l)) + '0' * k)
