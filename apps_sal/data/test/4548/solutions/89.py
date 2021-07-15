N, M, X = list(map(int,input().split()))
A = list(map(int, input().split())) 

zero_goal = 0
N_goal = 0

for i in A:
    if i < X:
        zero_goal = zero_goal + 1
    else:
        N_goal = N_goal + 1
print((min(zero_goal, N_goal)))

