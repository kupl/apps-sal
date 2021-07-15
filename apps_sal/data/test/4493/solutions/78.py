
c = [list(map(int,input().split())) for i in range(3)]

for i in range(0,2):
    if not c[0][0+i]-c[0][1+i] \
        == c[1][0+i]-c[1][1+i] \
        == c[2][0+i]-c[2][1+i]:
        print('No')
        break

    if not c[0+i][0]-c[1+i][0] \
        == c[0+i][1]-c[1+i][1] \
        == c[0+i][2]-c[1+i][2]:
        print('No')
        break
else:
    print('Yes')

