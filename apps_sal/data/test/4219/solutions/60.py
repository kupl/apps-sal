n = int(input())
a = []
xy = [[] for i in range(n)]
for i in range(n):
    a.append(int(input()))
    for j in range(a[i]):
        xy[i].append(list(map(int, input().split())))
ans = 0
for i in range(2**n):
    tf = [False for j in range(n)]
    for j in range(n):
        if (i >> j) & 1:
            tf[j] = True
    flag = False
    for j in range(n):
        for k in range(a[j]):
            if tf[j]:
                if xy[j][k][1] != tf[xy[j][k][0] - 1]:
                    flag = True
                    break
        if flag:
            break
    else:
        ans = max(ans, tf.count(True))
print(ans)
