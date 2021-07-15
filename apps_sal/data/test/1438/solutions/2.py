import sys

n, k = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))
ingr = list(map(int, sys.stdin.readline().split()))
ans = [[0,0,0] for i in range(n)]
for i in range(n):
    ans[i][0] = ingr[i]//lst[i]
    ans[i][1] = ingr[i]%lst[i]
    ans[i][2] = i
ans.sort(key = lambda x: [x[0],x[1]])
minn = ans[0][0]
while (k > 0):
    ans[0][1] += 1
    k -= 1
    if (ans[0][1] >= lst[ans[0][2]]):
        ans[0][0] += 1
        ans[0][1] = 0
    ans.sort(key = lambda x: [x[0],x[1]])
    if (ans[0][0] > minn):
        minn = ans[0][0]
print(minn)

