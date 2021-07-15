##n, m = [10,11]
##a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##s = [[3, 2],
##[3, 9],
##[2, 10],
##[3, 1],
##[3, 10],
##[1, 1, 10],
##[2, 10],
##[2, 10],
##[3, 1],
##[3, 10],
##[3, 9]]

n,m = [int(x) for x in input().split(' ')]
a = [int(x) for x in input().split(' ')]

s = []
for i in range(m):
    s.append( [int(x) for x in input().split(' ')] )


add = 0
for l in s:
    if l[0] == 1:
        v,x = int(l[1]), int(l[2])
        a[v-1] = x-add
    elif l[0] == 2:
        y = int(l[1])
        add += y
    elif l[0] == 3:
        print(a[int(l[1])-1]+add)

