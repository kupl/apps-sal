N, X, T = list(map(int, input().split()))
ans = 0
i = 0
while N - i * X > 0:
    ans += T
    i += 1

print(ans)
