n, c = list(map(int, input().split()))
# input時に前処理として以下のことをしておく
#   * 開始時間を-1(-0.5の制約だが、-1しても変わらないので-1する)しておく

# テレビ局の番組をチャンネルごとに登録
r = [[0 for i in range(c)] for j in range(100000)]
for _ in range(n):
    s,t,c = list(map(int, input().split()))
    for j in range(s-1, t):
        r[j][c - 1] = 1
# print(*r,sep='\n')

ans = 0
for i in range(len(r)):
    ans = max(ans, sum(r[i]))
print(ans)


# 補足
# チャンネル数4の場合以下のような配列ができる
# 1行でとある時間のチャンネル状態(1: 録画する, 0: 録画しない)がつく
#[0, 0, 0, 0]
#[0, 0, 1, 0]
#[1, 1, 1, 0]  <- この時間で3チャンネル録画が必要
#[1, 1, 0, 0]  <- この時間で2チャンネル録画が必要
#[1, 1, 0, 0]
#[1, 0, 0, 0]

