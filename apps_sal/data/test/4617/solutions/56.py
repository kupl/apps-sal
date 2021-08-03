# 文字列を取得
C1 = str(input())
C2 = str(input())

# 文字列の結合
ori_str = C1 + C2

# 末尾から１文字ずつ取得して逆さま文字を生成
rev_str = ori_str[-1::-1]

# 比較結果を出力
if ori_str == rev_str:
    print("YES")
else:
    print("NO")
