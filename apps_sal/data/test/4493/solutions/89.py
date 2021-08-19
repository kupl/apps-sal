c = [[0] * 3] * 3
for i in range(3):
    c[i] = [int(x) for x in input().split()]
ans = False
if c[0][0] - c[0][1] == c[1][0] - c[1][1] == c[2][0] - c[2][1] and c[0][0] - c[0][2] == c[1][0] - c[1][2] == c[2][0] - c[2][2]:
    ans = True
if ans == True:
    print('Yes')
else:
    print('No')
