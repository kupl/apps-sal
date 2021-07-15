l = list(map(int, input().split()))
A, B, C, X, Y = l[0], l[1], l[2], l[3], l[4]
s_1, s_2, s_3 = 0, 0, 0

s_1 = A*X + B*Y

maxv = max([X, Y])
s_2 = 2*C*max([X, Y])
if X >= Y:
    s_3 = 2*C*Y + A*(X-Y)
else:
    s_3 = 2*C*X + B*(Y-X)

print((min([s_1, s_2, s_3])))

