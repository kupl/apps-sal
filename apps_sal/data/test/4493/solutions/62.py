C = [list(map(int, input().split())) for _ in range(3)]
if not (C[0][0] - C[0][1] == C[1][0] - C[1][1] == C[2][0] - C[2][1]):
    print("No")
    return
if not (C[0][0] - C[0][2] == C[1][0] - C[1][2] == C[2][0] - C[2][2]):
    print("No")
    return
if not (C[0][2] - C[0][1] == C[1][2] - C[1][1] == C[2][2] - C[2][1]):
    print("No")
    return

print("Yes")
