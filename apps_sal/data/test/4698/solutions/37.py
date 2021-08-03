import copy
n = int(input())
li = list(map(int, input().split()))
lis = copy.copy(li)
m = int(input())
dri = [list(map(int, input().split())) for i in range(m)]
for i in range(len(dri)):
    lis = copy.copy(li)
    lis[dri[i][0] - 1] = dri[i][1]
    print(sum(lis))
