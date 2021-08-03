N, M = list(map(int, input().split()))
diff = [0 for _ in range(N + 1)]
for _ in range(M):
    L, R = list(map(int, input().split()))
    diff[L - 1] += 1
    diff[R] -= 1
ans = 0
x = 0
for i in range(N):
    x += diff[i]
    if x == M:
        ans += 1
print(ans)
