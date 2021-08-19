def gcd(x, y):
    while y > 0:
        (x, y) = (y, x % y)
    return x


N = int(input())
A = list(map(int, input().split()))
a = A[0]
for i in range(1, N):
    b = A[i]
    a = gcd(a, b)
print(a)
