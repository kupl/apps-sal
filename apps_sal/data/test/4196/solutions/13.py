def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
a = list(map(int, input().strip().split()))

L = [0]
R = [0]
for i in range(n):
    L.append(gcd(L[i], a[i]))
    R.append(gcd(R[i], a[n - i - 1]))

res = 0
for i in range(n):
    if res < gcd(L[i], R[n - i - 1]):
        res = gcd(L[i], R[n - i - 1])

print(res)
