

n, m = list(map(int, input().rstrip().split()))
data = []
for i in range(0, n):
    data.append(list(map(int, input().rstrip().split())))


def mergesortbysecond(l):
    if len(l) == 1:
        return l
    llower = []
    lupper = []
    for i in range(0, int(len(l) / 2)):
        llower.append(l[i])
    for i in range(int(len(l) / 2), len(l)):
        lupper.append(l[i])

    slower = mergesortbysecond(llower)
    supper = mergesortbysecond(lupper)

    b = 0
    u = 0
    sort = []
    while b < len(slower) and u < len(supper):
        if slower[b][1] <= supper[u][1]:
            sort.append(slower[b])
            b = b + 1
        elif supper[u][1] < slower[b][1]:
            sort.append(supper[u])
            u = u + 1
    if b == len(slower):
        for i in range(u, len(supper)):
            sort.append(supper[i])
    elif u == len(supper):
        for i in range(b, len(slower)):
            sort.append(slower[i])
    return sort


sort = mergesortbysecond(data)


bsort = []
for i in range(0, n):
    bsort.append(sort[n - i - 1])


dic = {}
for i in range(0, n):
    if bsort[i][0] in dic:
        dic[bsort[i][0]].append(bsort[i][1])
    else:
        dic[bsort[i][0]] = [bsort[i][1]]


array = []
for i in range(0, n):
    array.append([])


for ele in dic:
    j = 0
    for i in range(0, len(dic[ele])):
        j = j + dic[ele][i]
        array[i].append(j)


array


ma = 0

for i in range(0, len(array)):
    s = 0
    for j in range(0, len(array[i])):
        s = s + max([array[i][j], 0])

    if s > ma:
        ma = s


print(ma)
