N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += i * (N // i * (N // i + 1)) // 2
print(ans)
