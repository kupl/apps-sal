N, M = map(int, input().split())
ans = 0
if 2 * N <= M:
    ans += N
    M -= 2 * N
else:
    ans += (M // 2)
    M -= (M // 2) * 2
ans += (M // 4)
print(ans)
