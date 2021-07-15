N, M, X = map(int, input().split())
A = list(map(int, input().split()))

goal_N = 0
goal_0 = 0

for i in range(X, N + 1):
    if i in A:
        goal_N += 1

for i in range(0, X + 1):
    if i in A:
        goal_0 += 1

min_cost = min(goal_N,goal_0)

print(min_cost)
