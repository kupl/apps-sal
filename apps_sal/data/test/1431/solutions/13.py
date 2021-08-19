N = int(input())
a = list(map(int, input().split()))

# 1開始にする
A = [0] + a
# いい入れ方（1はボールが入っている）
B = [0] * (N + 1)
# ボールが入っている箱の番号
ans = []

# Nから1までループ
for i in range(N, 0, -1):
    # iの1つ目の倍数からNまでの倍数の箱にボールが入っている箱の個数を求める
    tmp = 0
    for j in range(i * 2, N + 1, i):
        tmp += B[j]

    # 合計%2がA[i]と不一致ならボールを入れる
    if tmp % 2 != A[i]:
        B[i] = 1
        ans.append(i)

if len(ans) == 0:
    print((0))
else:
    print((len(ans)))
    print((' '.join(map(str, ans))))
