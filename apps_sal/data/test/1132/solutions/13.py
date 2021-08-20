3
(n, m) = [int(x) for x in input().split()]
degree = {0: 0, 1: 0, 2: 0, n - 1: 0}
visited = [0] * n
adjlist = [[] for x in range(n)]
for i in range(m):
    (x, y) = [int(x) for x in input().split()]
    x -= 1
    y -= 1
    adjlist[x].append(y)
    adjlist[y].append(x)
for i in range(n):
    cur_degree = len(adjlist[i])
    if cur_degree not in degree:
        degree[cur_degree] = 1
    else:
        degree[cur_degree] += 1
degree_other = False
for val in list(degree.keys()):
    if val != 1 and val != 2 and (val != n - 1) and (val != 0):
        degree_other = True
if degree_other == True:
    print('unknown topology')
elif degree[1] == n - 1 and degree[n - 1] == 1:
    print('star topology')
elif degree[1] == 2 and degree[2] == n - 2:
    print('bus topology')
elif degree[2] == n:
    print('ring topology')
else:
    print('unknown topology')
