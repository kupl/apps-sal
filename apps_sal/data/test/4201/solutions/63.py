H, W, K = map(int, input().split())
c = [["." for _ in range(W)] for _ in range(H)]

for h in range(H):
    c[h] = input()

ans = 0
for i in range(2 ** H):
    for k in range(2 ** W):
        count = 0
    ## どの桁が1になっているかをチェックするために2進数の各桁をループ
        for h in range(H):
            for w in range(W):
        ## i >> jで確認したい桁を一番右までずらして1と論理積をとって「選択」している要素を確認
                if (i >> h) & 1 and (k >> w) & 1:
                    if c[h][w] == "#":
                        count += 1

        if count == K:
            ans += 1
print(ans)
