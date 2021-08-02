N = int(input())

ans = 0
for i in range(1, N + 1):
    y = N // i
    val = (y * (y + 1)) // 2
    ans += val * i

print(ans)
