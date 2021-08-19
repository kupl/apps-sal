A = [input() for i in range(8)]
B = 9
W = 9
for i in range(8):
    for j in range(8):
        if A[j][i] == 'W':
            W = min(W, j)
            break
        if A[j][i] == 'B':
            break
    for j in range(7, -1, -1):
        if A[j][i] == 'B':
            B = min(B, 8 - j)
            break
        if A[j][i] == 'W':
            break
if B <= W:
    print('B')
else:
    print('A')
