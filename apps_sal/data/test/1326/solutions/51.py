N = int(input())
ans = 0
for i in range(1, N + 1):
    cnt = N // i
    ans += cnt * (cnt + 1) // 2 * i
print(ans)
