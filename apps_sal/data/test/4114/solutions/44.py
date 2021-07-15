n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]

for i in range(101):
    for j in range(101):
        s = -1
        flag = True
        limit = float('inf')
        for x, y, h in xyh:
            if h != 0:
                H = h + abs(x-i) + abs(y-j)
                if s != -1:
                    if s != H:
                        flag = False
                        break
                s = H
            else:
                limit = min(limit, abs(x-i) + abs(y-j))
        if flag:
            if s != -1 and s <= limit:
                print(i, j, s)
                return
            elif s <= limit and limit == 1:
                print(i, j, 1)
                return
