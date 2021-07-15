# N 科目のテスト, K 点満点, 平均点 M 点以上
# 最後のテストで最低何点取る必要があるか : answer
# 達成不可能である場合は、代わりに -1 を出力

N, K, M = map(int, input().split())
scores = list(map(int, input().split()))

achieve_score = N * M
answer = achieve_score - sum(scores)

if answer <= 0:
    print(0)
elif answer <= K:
    print(answer)
else:
    print('-1')
