def get_sub_array(array):
    d = {}
    st = 0
    en = 0
    while st < len(array) and en < len(array):
        if en < (len(array) - 1) and array[en + 1] == array[en] + 1:
            en += 1
        else:
            d[array[st]] = en - st + 1
            st += 1
            en = st if en < st else en
    return d


n, m = [int(x) for x in input().split()]
array = []
for i in range(m):
    array.append([int(x) for x in input().split()])
d = dict()
for i in range(1, n + 1):
    d[array[0][i - 1]] = i
for i in range(m):
    for j in range(n):
        array[i][j] = d[array[i][j]]
res = [float("inf") for i in range(n)]
dm = []
for i in range(m):
    dm.append(get_sub_array(array[i]))
for i in range(1, n + 1):
    for j in range(m):
        res[i - 1] = min(res[i - 1], dm[j][i])
print(sum(res))
