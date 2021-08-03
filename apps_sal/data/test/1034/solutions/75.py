from heapq import heappop, heappush

# 入力の受付
X, Y, Z, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

# 入力配列のソート(降順: 大きい値が先頭)
a_list.sort(reverse=True)
b_list.sort(reverse=True)
c_list.sort(reverse=True)

# 優先度付きキューの定義
hq = []

# キューの管理リスト
arg_hash = {}

# キューの初期値
val = -(a_list[0] + b_list[0] + c_list[0])
heappush(hq, (val, 0, 0, 0))

# 答えを格納する配列
ans_arr = []

# 最大値を取り出していく．
# 以下をK回繰り返す
# 1. -(A+B+C)を要素とするキューの中の最小値を取り出す．(i番目に小さい数) この最小値は(A,B,C)の各リストの(p,q,r)番目のリストに含まれる値．
# 2．このキューに対して(p+1, q, r), (p, q+1, r), (p, q, r+1)のそれぞれが含まれているかどうかを確認
#     ない場合には，キューの管理リストに追加 & キューにその要素を追加
#     ある場合には，特に何もせず．
for i in range(K):
    # キューから最小値を取り出す(負なので実際は最大値を取り出している)
    ans_val, p, q, r = heappop(hq)
    ans_arr.append(-ans_val)

    # (p+1, q, r), (p, q+1, r), (p, q, r+1)のそれぞれが含まれているかどうかを確認
    arg_a = (p + 1, q, r)
    arg_b = (p, q + 1, r)
    arg_c = (p, q, r + 1)

    # キューの管理リストに対して，上の要素が存在するかどうかの探索と処理
    # a < X-1 は，全要素がキューに入っている場合に，さらに次のインデックスの要素を追加しないようにするための検索条件
    # p+1 用
    if (p < X - 1) and (arg_a not in arg_hash):
        # キュー管理リストに(p+1, q, r)のタプルを登録（辞書キーとして）
        arg_hash[arg_a] = 1
        # キューに値を登録
        heappush(hq, (-(a_list[p + 1] + b_list[q] + c_list[r]), ) + arg_a)
    # q+1 用
    if (q < Y - 1) and (arg_b not in arg_hash):
        # キュー管理リストに(p+1, q, r)のタプルを登録（辞書キーとして）
        arg_hash[arg_b] = 1
        # キューに値を登録
        heappush(hq, (-(a_list[p] + b_list[q + 1] + c_list[r]), ) + arg_b)
    # r+1 用
    if (r < Z - 1) and (arg_c not in arg_hash):
        # キュー管理リストに(p+1, q, r)のタプルを登録（辞書キーとして）
        arg_hash[arg_c] = 1
        # キューに値を登録
        heappush(hq, (-(a_list[p] + b_list[q] + c_list[r + 1]), ) + arg_c)

# 結果出力
for i in range(len(ans_arr)):
    print((ans_arr[i]))
