N = int(input())

ans = 0

for i in range(1, N + 1):
    ans += i * (1 + N // i) * (N // i) // 2

print(ans)
