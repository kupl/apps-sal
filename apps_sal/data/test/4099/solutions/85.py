# 高橋君N科目のテスト受ける
# 各テストK満点。0以上の整数。
# 高橋君N-1科目受講済み
# i番目の科目の点数はA1点　A＝list(map(int.input().split())使う
# 目標　N科目のテストの平均点をM以上にする。　最低点数N×M
# 目標達成の為には最後のテストで最低何点とる必要があるか出力せよ。　N科目×M点-総合点数A点
# 達成不可能な場合-1を出力。 print(-1)
#

# 入力
# N K M
# A1 A2…An-1
# 出力
# 最後のテストでの必要最低点または-1


N,K,M = map(int,input().split())
A = list(map(int,input().split()))

if 0 <= (N*M)-sum(A) <= K:
    print((N*M)-sum(A))

elif K < (N*M)-sum(A):
    print(-1)

else:  # 0でも達成
   print(0)
