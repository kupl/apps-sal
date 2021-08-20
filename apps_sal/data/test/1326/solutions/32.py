N = int(input())
ans = 0
for i in range(1, N + 1):
    x = N // i
    ans += i * x * (x + 1) // 2
print(ans)
