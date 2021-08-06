n, m = [int(x) for x in input().split()]
p = 10 ** 9 + 7

x = [0] * max(n, m)
x[0:1] = [1, 2]
for i in range(2, max(n, m)):
    x[i] = (x[i - 1] + x[i - 2]) % p

print(2 * (x[n - 1] + x[m - 1] - 1) % p)
