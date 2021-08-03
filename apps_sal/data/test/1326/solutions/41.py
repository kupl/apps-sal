N = int(input())
ans = 0
for i in range(1, N + 1):
    M = N // i
    ans += M * (M + 1) // 2 * i
print(ans)
