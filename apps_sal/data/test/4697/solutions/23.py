N, M = list(map(int, input().split()))
total = 2 * N + M
ans = total // 4
if ans * 2 > M:
    ans = M // 2
print(ans)
