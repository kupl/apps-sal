(N, D) = list(map(int, input().split()))
ans = 0
for i in range(N):
    (X, Y) = list(map(int, input().split()))
    dis = (X * X + Y * Y) ** 0.5
    if dis <= D:
        ans += 1
print(ans)
