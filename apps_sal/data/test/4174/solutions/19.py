import bisect
n, x = map(int, input().split())
Y = list(map(int, input().split()))
Z = [0] * n
a = 0
for i in range(n):
    a += Y[i]
    Z[i] = a
print(1 + bisect.bisect_left(Z, x + 1))
