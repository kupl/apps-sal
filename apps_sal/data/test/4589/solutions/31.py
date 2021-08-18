H, W = map(int, input().split())
S = [input() for i in range(H)]

for h in range(H):
    new_s = ''
    for w in range(W):
        if S[h][w] == '
        new_s += '
        continue
        count = 0
        ary = [-1, 0, 1]
        for i in ary:
            for j in ary:
                if h + i < 0 or h + i >= H or w + j < 0 or w + j >= W:
                    continue
                if S[h + i][w + j] == '
                count += 1
        new_s += str(count)

    S[h] = new_s

for s in S:
    print(s)
