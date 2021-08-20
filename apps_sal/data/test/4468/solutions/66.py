(N, T) = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    if t[i + 1] - t[i] > T:
        ans += T
    else:
        ans += t[i + 1] - t[i]
ans += T
print(ans)
