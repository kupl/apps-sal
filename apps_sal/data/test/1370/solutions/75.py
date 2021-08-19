import sys
input = sys.stdin.readline

H, W, K = list(map(int, input().split()))
S = [input().rstrip() for _ in range(H)]

bit = 2**(H - 1)  # bit全探索　横方向の割方をすべて見る
ans = (H - 1) + (W - 1)  # ここミスるとTLE float('inf')はダメ。10**5もダメ。
for bi in range(bit):
    w = 0
    cnt = bin(bi).count('1')  # 横割の数
    white = [0] * H  # 縦割りの数を貪欲に求める

    while w < W:
        i = 0
        for h in range(H):
            if S[h][w] == '1':
                white[i] += 1
                if white[i] > K:  # 超えたら割数を足す。カウンタを初期化、超えた列をもう一度足す
                    cnt += 1
                    white = [0] * H
                    w -= 1
                    break
            if bi >> h & 1:
                i += 1
        w += 1
        if cnt >= ans:  # すでにansを超えてたらやめる。これがないとTLE
            break
    ans = min(ans, cnt)  # 小さければ更新
print(ans)
