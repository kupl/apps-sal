M = 10**9 + 7
n, k = map(int, input().split())
l = [1]
f = 1
for i in range(n):
    f = f * (i + 1) % M
    l += [f]
a = 0
for i in range(min(n, k + 1)):
    c = p = 1
    c = c * l[n] * l[n - 1] % M
    p = p * l[i]**2 * l[n - i] * l[n - i - 1] % M
    a += c * pow(p, M - 2, M)
print(a % M)
