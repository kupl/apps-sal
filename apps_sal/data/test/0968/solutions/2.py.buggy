from sys import *
n = int(input())
names = []
for i in range(n):
    names.append(input().split())
p = [names[x - 1] for x in list(map(int, input().split()))]
curr_handle = min(p[0][0], p[0][1])
for i in range(1, n):
    if curr_handle > p[i][0] and curr_handle > p[i][1]:
        print("NO")
        return
    else:
        min_curr = min(p[i][0], p[i][1])
        curr_handle = min_curr if curr_handle <= min_curr else max(p[i][0], p[i][1])
print("YES")
