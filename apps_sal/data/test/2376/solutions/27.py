from collections import defaultdict
(N, W) = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
DP = defaultdict(int)
DP[0] = 0
for (weight, value) in wv:
    exists = list(DP.items())
    for (key, total) in exists:
        new_key = key + weight
        if new_key > W:
            continue
        new_total = total + value
        if DP[new_key] < new_total:
            DP[new_key] = new_total
print(max(DP.values()))
