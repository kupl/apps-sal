g = [[1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11], [2]]
x, y = map(int, input().split())
for i in range(len(g)):
    if x in g[i]:
        xg = i
    if y in g[i]:
        yg = i
if xg == yg:
    print('Yes')
else:
    print('No')
