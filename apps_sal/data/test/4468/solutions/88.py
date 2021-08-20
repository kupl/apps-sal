(N, T) = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = 0
for i in range(0, N - 1):
    if t[i] + T > t[i + 1]:
        ans += t[i + 1] - t[i]
    else:
        ans += T
ans += T
print(ans)
