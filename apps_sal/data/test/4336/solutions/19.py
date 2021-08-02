W, H, x, y = list(map(float, input().split()))

ans = W * H
ans = float(float(ans) / 2.0)
ans2 = 0
if x == float(float(W) / 2) and y == float(float(H) / 2):
    ans2 = 1

print(str(ans) + " " + str(ans2))
