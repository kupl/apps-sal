R, n, x, p, v = 10 ** 9 + 7, int(input()), sorted(map(int, input().split())), [1], 0
for i in range(1, n):
    p.append(2 * p[-1] % R)
print(sum((x[i] - x[i - 1]) * (p[i] - 1) * (p[n - i] - 1) for i in range(1, n)) % R)
