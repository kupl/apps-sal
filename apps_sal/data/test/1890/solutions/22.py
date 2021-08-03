A = input()
n = int(input())
m = 1000000007
a = len(A)

x = pow(2, a * n, m) - 1 + m
y = pow(2, a, m) - 1 + m
f = x * pow(y, m - 2, m) % m

s = 0
for r in range(a):
    if A[r] in '05':
        s = (s + pow(2, r, m)) % m
print((s * f) % m)
