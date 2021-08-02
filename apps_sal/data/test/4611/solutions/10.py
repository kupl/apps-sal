# https://atcoder.jp/contests/abc086/tasks/arc089_a
n = int(input())
txy = [list(map(int, input().split())) for _ in range(n)]

px, py = (0, 0)
pt = 0

for t, x, y in txy:
    if not (x + y <= t and (x + y) % 2 == t % 2 and abs(x - px) + abs(y - py) <= t - pt):
        print('No')
        return
    px, py = x, y
    pt = t

print('Yes')
