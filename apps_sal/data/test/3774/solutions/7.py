n, m = sorted(map(int, input().split()))
print(n * m - {1: min(m % 6, 6 - m % 6), 2: {2: 4, 3: 2, 7: 2}.get(m, 0)}.get(n, n & 1 * m & 1))
