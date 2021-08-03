# キューのクラス
class Queue:
    def __init__(self, data=[]):
        self.data = data

    def enqueue(self, x):
        self.data.append(x)
        return self.data

    def dequeue(self):
        if len(self.data) == 0:
            return "Queue is Empty!"
        else:
            cell = self.data[0]
            del self.data[0]
            return self.data


H, W = list(map(int, input().split()))
s = [list(input()) for i in range(H)]
# 4近傍探索のために用意
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# 最小距離のリスト(Falseで初期化)
min_dis = [[False for i in range(W)] for j in range(H)]
min_dis[0][0] = 1  # スタート位置を1にする(注意!!)
# キューのインスタンスQ作成
Q = Queue()
Q.enqueue([0, 0])
# キューの中身がなくなるまでループ
while Q.data:
    y = Q.data[0][0]
    x = Q.data[0][1]
    # 4近傍探索
    for i, j in zip(dy, dx):
        if (0 <= y + i < H) and (0 <= x + j < W) and s[y + i][x + j] == ".":  # （範囲内にあった場合）かつ（道だった場合）
            if min_dis[y + i][x + j] == False:  # 最小距離がFalseだった場合
                min_dis[y + i][x + j] = min_dis[y][x] + 1
                Q.enqueue([y + i, x + j])  # 値を更新したマスをQにプッシュ
    Q.dequeue()  # 探索し終わったマスをQからプル

if not min_dis[H - 1][W - 1]:
    print((-1))
    return

# マスをカウント
num_shap = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            num_shap += 1
# スコア＝（全マス)-(#マス)-(gへの最短経路)
score = (H * W) - num_shap - (min_dis[H - 1][W - 1])
print(score)
