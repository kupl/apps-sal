# 高橋君の夏休みは N 日間
# 夏休みの宿題が M 個
# 遊ぶことができる日数は？
# ただし、夏休み中に全ての宿題を終わらせることができないときは、-1 を出力

N, M = map(int, input().split())
A = list(map(int, input().split()))

answer = N - sum(A)

if N >= sum(A):
    print(answer)

else:
    print('-1')
