from collections import defaultdict
h, w, d = map(int, input().split())

G = defaultdict(list)
for i in range(h):
    l = list(map(int, input().split()))
    for n, item in enumerate(l):
        G[item] = [n, i]


dp = [0 for i in range(h * w + 1)]
for i in range(d):
    current_place = i + 1
    while current_place + d <= h * w:
        x, y = G[current_place]
        next_place = current_place + d
        x1, y1 = G[next_place]
        magic = abs(x - x1) + abs(y - y1)
        dp[next_place] = magic + dp[current_place]
        current_place = next_place

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(dp[r] - dp[l], flush=True)
