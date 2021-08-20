(n, m, k) = map(int, input().split())
k -= 1
print(k // (2 * m) + 1, k % (2 * m) // 2 + 1, 'L' if k % 2 == 0 else 'R')
