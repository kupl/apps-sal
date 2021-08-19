import copy
n = int(input())
t = [int(x) for x in input().split()]
m = int(input())
p = []
for i in range(m):
    p.append([int(x) for x in input().split()])
for i in range(m):
    r = copy.copy(t)
    r[p[i][0] - 1] = p[i][1]
    print(sum(r))
