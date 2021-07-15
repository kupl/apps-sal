#18 C - Takahashi's Information
c = [list(map(int,input().split())) for _ in range(3)]

cnt = 0
if (c[0][0] - c[1][0]) == (c[0][1] - c[1][1]) == (c[0][2] - c[1][2]):
    cnt += 1
if (c[1][0] - c[2][0]) == (c[1][1] - c[2][1]) == (c[1][2] - c[2][2]):
    cnt += 1
if (c[2][0] - c[0][0]) == (c[2][1] - c[0][1]) == (c[2][2] - c[0][2]):
    cnt += 1
if cnt == 3:
    print('Yes')
else:
    print('No')
