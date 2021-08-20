xx = []
(n, k) = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
xx = sorted(ab, key=lambda x: x[0])
ans = 0
for i in range(n):
    ans += xx[i][1]
    if ans >= k:
        print(xx[i][0])
        break
