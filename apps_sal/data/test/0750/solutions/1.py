n, k = map(int, input().split())
ans = 0
ans += (2 * n) // k + bool((2 * n) % k != 0)
ans += (5 * n) // k + bool((5 * n) % k != 0)
ans += (8 * n) // k + bool((8 * n) % k != 0)
print(ans)
