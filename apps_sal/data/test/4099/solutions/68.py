# 高橋君　N科目のテストを受ける
# Kは満点
# Mは平均点
#　Aは取ったスコアのリスト
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

#　必要なスコアの計算
need_score = N * M - sum(A)

#　need_scoreがKより大きいとき
if K >= need_score:
    if need_score <=0:
        print(0)
    else:
        print(need_score)
# need_scoreがKより小さいので、挽回不可
else:
    print(-1)
