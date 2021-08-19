from collections import defaultdict, deque

h, w = map(int, input().split())
tizu = [input() for _ in range(h)]
ans = 0
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for i in range(h):
    for j in range(w):
        if tizu[i][j] == "#":
            continue
        check = [[False for _ in range(w)] for _ in range(h)]
        check[i][j] = True
        queue = deque()
        queue.append([i, j])
        queue.append(0)
        while queue:
            pos = queue.popleft()
            ans_sub = queue.popleft()
            for dh, dw in directions:
                nh = pos[0] + dh
                nw = pos[1] + dw
                if nh == -1 or nh == h or nw == -1 or nw == w:
                    continue
                if tizu[nh][nw] == "#":
                    continue
                if check[nh][nw]:
                    continue
                check[nh][nw] = True
                queue.append([nh, nw])
                queue.append(ans_sub + 1)
        ans = max(ans, ans_sub)
print(ans)
