(n, k) = map(int, input().split())
print(*list(reversed(range(1, k + 2))) + list(range(k + 2, n + 1)))
