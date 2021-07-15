
INF = 1<<60
def resolve():
    def judge(j):
        for i in range(group):
            cnt_Wchoco[i] += div_G[i][j]
            if cnt_Wchoco[i] > K:
                return False
        return True

    H, W, K = list(map(int, input().split()))
    G = [list(map(int, input())) for _ in range(H)]

    ans = INF
    for bit in range(1<<(H-1)):
        group = 0 # 分かれたブロック数
        row = [0]*H
        for i in range(H):
            # 分割ライン
            row[i] = group
            if bit>>i & 1:
                group += 1
        group += 1 # 1つ折ったら2つに分かれるのでプラス1, 折らなかったら1つ

        # 分割したブロックを列方向で見る
        div_G = [[0] * W for _ in range(group)]
        for i in range(H):
            for j in range(W):
                div_G[row[i]][j] += G[i][j]

        num = group-1
        cnt_Wchoco = [0]*group
        for j in range(W):
            if not judge(j):
                num += 1
                cnt_Wchoco = [0] * group
                if not judge(j):
                    num = INF
                    break
        ans = min(ans, num)

    print(ans)

def __starting_point():
    resolve()

__starting_point()
