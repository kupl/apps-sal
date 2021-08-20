c = [list(map(int, input().split())) for _ in range(3)]
A1 = c[1][0] - c[0][0]
A2 = c[2][0] - c[1][0]
B1 = c[0][1] - c[0][0]
B2 = c[0][2] - c[0][1]
if c[1][1] == A1 + B1 + c[0][0] and c[1][2] == A1 + B1 + B2 + c[0][0] and (c[2][1] == A1 + A2 + B1 + c[0][0]) and (c[2][2] == A1 + A2 + B1 + B2 + c[0][0]):
    print('Yes')
else:
    print('No')
