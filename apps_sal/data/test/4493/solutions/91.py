a = []
for i in range(3):
    a.append(list(map(int, input().split())))
if a[1][0] - a[0][0] == a[1][1] - a[0][1] == a[1][2] - a[0][2] and a[2][0] - a[0][0] == a[2][1] - a[0][1] == a[2][2] - a[0][2]:
    print('Yes')
else:
    print('No')
