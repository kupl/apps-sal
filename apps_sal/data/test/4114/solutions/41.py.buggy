import sys

input = sys.stdin.readline
N = int(input())
piramids = []
for _ in range(N):
    x, y, h = map(int, input().split())
    piramids.append((x, y, h))

for cx in range(101):
    for cy in range(101):
        h_cands = set()
        for x, y, h in piramids:
            if h == 0:
                continue
            cand = h + abs(x - cx) + abs(y - cy)
            h_cands.add(cand)

        # 制約として必ず特定できる
        if len(h_cands) == 1:
            for x, y, h in piramids:
                if h != max(cand - abs(x - cx) - abs(y - cy), 0):
                    break
            else:
                print(cx, cy, cand)
                return
