(n, m) = map(int, input().split())
X = [list(map(int, input().split())) for i in range(m)]
a_list = []
b_list = []
for i in range(m):
    if X[i][0] == 1:
        a_list.append(X[i][1])
    elif X[i][1] == n:
        b_list.append(X[i][0])
c_set = set(a_list) & set(b_list)
if len(c_set) == 0:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
