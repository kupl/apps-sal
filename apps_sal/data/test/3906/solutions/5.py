n, m = [int(x) for x in input().split()]
p = 10 ** 9 + 7

x = [1, 2]
for i in range(2, max(n, m)):
    x.append(x[i - 1] + x[i - 2])

print(2 * (x[n - 1] + x[m - 1] - 1) % p)

