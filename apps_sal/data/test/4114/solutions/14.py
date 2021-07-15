n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]

test = [(x,y,h) for x,y,h in xyh if h > 0]
test = test[0]
for cx in range(101):
    for cy in range(101):
        # h > 0で中心座標の高さを見積もる
        x,y,h = test
        H = h + abs(x - cx) + abs(y - cy)

        # 全データに適合するか        
        if all([max(H - abs(x - cx) - abs(y - cy), 0) == h for x,y,h in xyh]):
            print(cx, cy, H)
            return
