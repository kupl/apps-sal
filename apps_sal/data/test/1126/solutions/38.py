(n, x, m) = map(int, input().split())
(l, k, i, j) = ([-1] * m, [], 0, -1)
while j < 0:
    l[x] = i
    k += [x]
    x = x ** 2 % m
    i += 1
    j = l[x]
n -= i
r = i - j
print(n // r * sum(k[j:]) + sum(k + k[j:n % r + j]))
