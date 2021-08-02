n = int(input())
Graph = [0] * n
for i in range(1, n):
    data = [int(s) for s in input().split()]
    Graph[data[0] - 1] += 1
    Graph[data[-1] - 1] += 1
flag = True
for i in Graph:
    if i == 2:
        flag = False
if flag == True:
    print("YES")
else:
    print("NO")
