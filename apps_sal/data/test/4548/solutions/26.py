# 入力
n, m, x = map(int, input().split())
a = list(map(int, input().split()))


goto_goal_0 = 0  # 0までのコスト
goto_goal_n = 0  # nまでのコスト

# x から 0 へ向かうコストを計算
for i in range(x - 1, 0, -1):   # x-1 番目から順番にデクリメントしながらforループ
    if i in a:
        goto_goal_0 += 1
        # print("0 is {}".format(goto_goal_0))

# x から n へ向かうコストを計算
for i in range(x, n + 1):   # x 番目から順番にインクリメントしながらforループ
    if i in a:
        goto_goal_n += 1
        # print("n is {}".format(goto_goal_n))

if goto_goal_0 < goto_goal_n:
    print(goto_goal_0)
else:
    print(goto_goal_n)
