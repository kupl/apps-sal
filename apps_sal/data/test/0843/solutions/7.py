import sys
def dfs(v):
    used[v] = True
    for i in ed[v]:
        if not used[i]:
            dfs(i)



sys.setrecursionlimit(1000000)
n = int(input())
data1 = input()
data2 = list(map(int, input().split()))
used = [False for i in range(n)]
data3 = [None for i in range(n)]
for i in range(n):
    if data1[i] == ">":
        data3[i] = i + data2[i]
    else:
        data3[i] = i - data2[i]
ans = True
index = 0
prev = -1
for i in range(2 * n):
    used[index] = True
    prev = index
    if data3[index] >= n or data3[index] < 0:
        ans = False
        break
    else:
        index = data3[index]
        if index == prev:
            break
if ans:
    print("INFINITE")
else:
    print("FINITE")
