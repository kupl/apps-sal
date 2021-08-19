N = int(input())
ans = 0
for j in range(1, N + 1):
    n = N // j
    ans += n * (2 * j + (n - 1) * j) // 2
print(ans)
