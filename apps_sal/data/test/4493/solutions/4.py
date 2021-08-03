C = [list(map(int, input().split())) for i in range(3)]
Bs = [C[0][i] for i in range(3)]
As = [0, C[1][0] - Bs[0], C[2][0] - Bs[0]]
if all(As[i] + Bs[j] == C[i][j] for i in range(3) for j in range(3)):
    print("Yes")
else:
    print("No")
