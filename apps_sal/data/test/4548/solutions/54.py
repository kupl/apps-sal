(n, m, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
goto_goal_0 = 0
goto_goal_n = 0
for i in range(x - 1, 0, -1):
    if i in a:
        goto_goal_0 += 1
for i in range(x, n + 1):
    if i in a:
        goto_goal_n += 1
if goto_goal_0 < goto_goal_n:
    print(goto_goal_0)
else:
    print(goto_goal_n)
