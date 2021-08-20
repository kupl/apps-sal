(N, T) = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = 0
for i in range(N):
    if i == 0:
        continue
    if t[i] - t[i - 1] < T:
        ans += t[i] - t[i - 1]
    else:
        ans += T
ans += T
print(ans)
