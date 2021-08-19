N = int(input())
K = int(input())
ans = 1
for _ in range(N):
    if ans + K < 2 * ans:
        ans += K
    else:
        ans *= 2
print(ans)
