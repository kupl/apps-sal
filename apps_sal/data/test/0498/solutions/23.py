(n, m, k) = map(int, input().split())
print((k - 1) // (2 * m) + 1, ((k - 1) % (2 * m) + 2) // 2, 'R' if ((k - 1) % (2 * m) + 1) % 2 == 0 else 'L')
