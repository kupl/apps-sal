(W, a, b) = map(int, input().split())
if abs(a - b) < W:
    ans = 0
else:
    ans = abs(a - b) - W
print(ans)
