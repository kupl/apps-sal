(W, H, N) = list(map(int, input().split()))
ans = [0, W, 0, H]
for i in range(N):
    (x, y, a) = list(map(int, input().split()))
    if a == 1:
        if ans[0] < x:
            ans[0] = x
    elif a == 2:
        if ans[1] > x:
            ans[1] = x
    elif a == 3:
        if ans[2] < y:
            ans[2] = y
    elif ans[3] > y:
        ans[3] = y
S = (ans[1] - ans[0]) * (ans[3] - ans[2])
if ans[1] - ans[0] < 0:
    print(0)
elif ans[3] - ans[2] < 0:
    print(0)
else:
    print(S)
