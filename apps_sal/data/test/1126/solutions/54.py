n, x, m = map(int, input().split())
r, l, k = n, [-1] * m, []
for i in range(n):
    j = l[x]
    if j >= 0:
        r = i - j
        break
    l[x] = i
    k += [x]
    x = x**2 % m
    n -= 1
print(n // r * sum(k[j:]) + sum(k + k[j:n % r + j]))
