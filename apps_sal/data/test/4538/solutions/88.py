(n, d) = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]
(x, y) = [list(i) for i in zip(*xy)]
d_2 = d ** 2
ans = 0
for i in range(n):
    if d_2 >= x[i] ** 2 + y[i] ** 2:
        ans += 1
print(ans)
