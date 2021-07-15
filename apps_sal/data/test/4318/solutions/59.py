# abc124b
# https://atcoder.jp/contests/abc124/tasks/abc124_b

# 東西にN個の山がある
# 西からi番目の山の高さはHi
# 西からi番目の山頂にある旅館からは必ず海が見れる
# 西からi(i=2, 3,...,N)番目の山頂にある旅館については、
# H1<Hi、H2<Hi...かつHi-1<Hiのとき、海が見れる

# N子の旅館のうち、海がみられるのは何個か

# max:最大値を求める関数

# 入力
n = int(input())
h = list(map(int, input().split()))

# 処理
# 山の高さを格納する
h_list = [h[0]]
# 海が見える旅館のカウント
ans = 1

for i in range(1, n):
    h_list.append(h[i])
    # 既存のリストの最大値の山の高さ以上の時
    if h[i] >= max(h_list):
        # 海が見える旅館の数を加算
        ans += 1

print(ans)


