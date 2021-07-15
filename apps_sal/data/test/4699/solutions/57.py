# N, Kの入力受付
N, K = map(int, input().split())
# Dの入力受付
D = set(input().split())
# 0-9とDの差集合作成、リスト化してEに代入
E = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"} - D
# Nに1ずつ足して条件に合う最初の数字を特定する
result = False
while result == False:
    for i in str(N):
        if not i in E:
            N = N + 1
            result = False
            break
        else:
            result = True
print(N)
