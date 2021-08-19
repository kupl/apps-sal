S_list = [input() for i in range(2)]
(N, M, X) = map(int, S_list[0].split())
A_list = list(map(int, S_list[1].split()))
A_goal_N = [i for i in A_list if X < i and i < N]
A_goal_0 = [i for i in A_list if 0 < i and i < X]
result = min(len(A_goal_N), len(A_goal_0))
print(result)
