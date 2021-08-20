v = [[0] * 2 for i in range(3)]
for i in range(3):
    v[i][1] = i
(v[0][0], v[1][0], v[2][0]) = map(int, input().split())
ways = [[0] * 3 for i in range(3)]
v.sort(reverse=True)
cord = [0] * 3
for i in range(3):
    for j in range(3):
        if v[j][1] == i:
            cord[j] = i
check = False
for i in range(v[1][0], 0, -1):
    if v[0][0] - i + v[1][0] - i == v[2][0]:
        ways[cord[0]][cord[1]] = i
        ways[cord[1]][cord[2]] = v[1][0] - i
        ways[cord[2]][cord[0]] = v[0][0] - i
        ways[cord[1]][cord[0]] = i
        ways[cord[2]][cord[1]] = v[1][0] - i
        ways[cord[0]][cord[2]] = v[0][0] - i
        check = True
        break
if check:
    print(ways[0][1], ways[1][2], ways[2][0])
else:
    print('Impossible')
