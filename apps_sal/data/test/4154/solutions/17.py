N, M = map(int, input().split())
Min = 1
Max = N
for i in range(M):
    L, R = map(int, input().split())
    if Min <= L and R <= Max:
        Min, Max = L, R
    elif Min <= R and R <= Max:
        Max = R
    elif Min <= L and L <= Max:
        Min = L
    elif L <= Min and Max <= R:
        pass
    else:
        Max, Min  = 0, 1
        break
print(Max - Min +1)
