H, W = map(int, input().split())
S = [list(input()) for i in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w] in ['.', 'B']:
            continue

        ary = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        flag = False
        for x, y in ary:
            xd = h + x
            yd = w + y
            if xd < 0 or xd >= H or yd < 0 or yd >= W:
                continue
            if S[xd][yd] in ['B', '#']:
                S[h][w] = 'B'
                S[xd][yd] = 'B'
                flag = True

        if not flag:
            print('No')
            return

print('Yes')
