import math

n, w = input().split(" ")
n = int(n)
w = int(w)

lis = [[int(j), 0] for j in input().split(" ")]
for i in range(n):
    lis[i][1] = i

lis = sorted(lis, key=lambda a: a[0], reverse=True)
f = True
ans = [0 for i in range(n)]
# print(ans)
for i in range(n):
    w -= math.ceil(lis[i][0] / 2)
    ans[lis[i][1]] = math.ceil(lis[i][0] / 2)
    if(w < 0):
        f = False
        break

# print(ans)
if(f == True):
    if(w == 0):
        for i in range(n):
            print(ans[i], end=" ")
    else:
        for i in range(n):
            if(w == 0):
                break
            if(w >= lis[i][0] - ans[lis[i][1]]):
                w -= lis[i][0] - ans[lis[i][1]]
                ans[lis[i][1]] = lis[i][0]
            else:
                ans[lis[i][1]] += w
                w = 0
        for i in range(n):
            print(ans[i], end=" ")
else:
    print(-1)
