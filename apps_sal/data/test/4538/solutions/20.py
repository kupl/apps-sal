(N, D) = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
D = D ** 2
ans = 0
for (x, y) in XY:
    if x ** 2 + y ** 2 <= D:
        ans += 1
print(ans)
