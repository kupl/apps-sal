N = int(input())
a = [0] * N
xy = [[]] * N
for i in range(N):
    a[i] = int(input())
    xy[i] = [list(map(int, input().split())) for _ in range(a[i])]
ans = 0
for i in range(2 ** N):
    tf = [False] * N
    for j in range(N):
        if i >> j & 1:
            tf[j] = True
    flag = False
    for j in range(N):
        for k in xy[j]:
            if tf[j] and k[1] != tf[k[0] - 1]:
                flag = True
                break
        if flag:
            break
    if flag:
        continue
    ans = max(ans, tf.count(True))
print(ans)
