import copy
n = int(input())
x = list(map(int,input().split()))
a = copy.deepcopy(x)
x.sort()
for i in range(n):
    if x[int(n/2)-1]<a[i]:
        print((x[int(n/2)-1]))
    else:
        print((x[int(n/2)]))

