H, W = list(map(int, input().split()))
ans = 0
for i in range(2):
    if H >= W:
        ans += H
        H -= 1
    else:
        ans += W
        W -= 1
print(ans)
