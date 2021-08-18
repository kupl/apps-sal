h, w, d = map(int, input().split())
a = {}
for y in range(h):
    line = list(map(int, input().split()))
    for x in range(len(line)):
        a[line[x] - 1] = (y, x)


num = len(a)
dp = [0] * num
for i in range(num - 1, -1, -1):
    if i + d <= num - 1:
        x, y = a[i]
        px, py = a[i + d]
        dp[i] = dp[i + d] + abs(x - px) + abs(y - py)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(dp[l] - dp[r])
