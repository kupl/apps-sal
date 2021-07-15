M = 0x3b9aca09
inv = lambda x: pow(x, M - 2, M)
n, a, b, k = list(map(int, input().split()))
s = input()
c = inv(a) * b % M
q = pow(c, k, M)
m = (n + 1) // k
p = (pow(q, m, M) - 1) * inv(q - 1) % M if q - 1 else m
x = pow(a, n, M)
r = 0
for i in range(k):
    r = (r + [-1, 1][s[i] == '+'] * x * p) % M
    x = (x * c) % M
print(r)

