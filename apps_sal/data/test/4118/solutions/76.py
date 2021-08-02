N = list(map(int, input().strip().split()))
state = -1
if(N[0] >= 1 and N[0] <= 9 and N[1] >= 1 and N[1] <= 9):
    state = N[0] * N[1]
print(state)
