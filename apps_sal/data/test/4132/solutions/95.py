N = int(input())
A = list(map(int, input().split()))


def gcd(x, y):
    if x < y:
        t = x
        x = y
        y = t
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


a = gcd(A[0], A[1])
for i in range(2, N):
    a = gcd(a, A[i])
print(a)
