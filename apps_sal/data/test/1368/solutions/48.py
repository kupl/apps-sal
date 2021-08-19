from math import factorial
(N, A, B) = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=1)
s = sum(v[:A])
print(s / A)
t = v[A - 1]
(p, q) = (0, 0)
for i in v:
    if i > t:
        p += 1
    elif i == t:
        q += 1
a = 0


def c(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


for i in range(A, B + 1):
    if p + q >= i:
        a += c(q, i - p)
    if t != v[0]:
        break
print(a)
