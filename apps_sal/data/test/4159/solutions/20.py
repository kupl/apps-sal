# 入力を受け取る
A,B,K = map(int,input().split())

# 条件分岐に応じて式をつくる
ret_A = A
ret_B = B

if A+B<=K:
    ret_A = 0
    ret_B = 0
elif A<=K<=A+B:
    ret_A = 0
    ret_B = B-(K-A)
else:
    ret_A = A-K
    ret_B = B

# 結果を出力する
print(ret_A, ret_B, sep=' ')
