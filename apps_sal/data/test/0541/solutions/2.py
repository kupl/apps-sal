n, m = map(int, input().split())
c = [[0] * 2 for _ in range(m)]
for i in range(m):
    c[i][1], c[i][0] = map(int, input().split())
c.sort()  # 橋を取り除く時はできるだけbの島に近いところで取り除くと良い。
x = -1  # 直前に取り除いた橋のindex
ans = 0
for i in range(m):
    if c[i][1] > x:
        x = c[i][0] - 1
        ans += 1
print(ans)
