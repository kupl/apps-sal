N, X, Y = list(map(int, input().split()))

dis_list = [0] * (N - 1)

# Xからの距離を求める
dis_X = [0] * N

for i in range(N):
    dis_X[i] = min(abs(X - (i + 1)), abs(Y - (i + 1)) + 1)

#
    # スタート位置
for start in range(N):
    for goal in range(start + 1, N):
        dis = min(abs(X - (start + 1)) + abs(Y - (goal + 1)) + 1, goal - start)
        dis_list[dis - 1] += 1

for ans in dis_list:
    print(ans)
