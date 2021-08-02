# 高橋君の夏休みは N 日間です。
# 夏休みの宿題が M 個出されており
# i 番目の宿題をやるには Ai 日間かかります。
# 夏休み中に全ての宿題を終わらせるぉとができないときは、かわりに '-1' を出力

N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) > N:
    print(-1)
else:
    print(N - sum(A))
