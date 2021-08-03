n, x, m = map(int, input().split())
l, k, i, j = [-1] * m, [], 0, -1
while j < 0:
    l[x] = i
    k += [x]
    x = x**2 % m
    n -= 1
    j = l[x]
    i += 1
r = i - j
print(n // r * sum(k[j:]) + sum(k + k[j:n % r + j]))
