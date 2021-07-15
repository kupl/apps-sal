v = []
for i in range(0, 8):
    x, y = list(map(int, input().split()))
    v.append((x, y))

v.sort()
if v[0][0] == v[1][0] == v[2][0] and v[3][0] == v[4][0] and v[5][0] == v[6][0] == v[7][0] and v[0][1] == v[3][1] == v[5][1] and v[1][1] == v[6][1] and v[2][1] == v[4][1] == v[7][1] and v[0][0] != v[3][0] != v[7][0] and v[0][1] != v[1][1] != v[2][1]: print('respectable')
else: print('ugly')

