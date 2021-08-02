N, T = map(int, input().rstrip().split(" "))
t = list(map(int, input().rstrip().split(" ")))
ans = 0
for i in range(N - 1):
    ans += min(T, t[i + 1] - t[i])
ans += T
print(ans)
