
n,k = list(map(int,input().split()))

m = list(map(int,input().split()))
c = list(map(int,input().split()))

mi = []
for i in range(n):
    mi.append([m[i],i])
mi.sort()
mi.reverse()

ans = [[]]

for loop in range(n):

    now,ind = mi[loop]

    l = -1
    r = len(ans)

    while r-l != 1:

        mid = (l+r)//2
        if len(ans[mid]) < c[now-1]:
            r = mid
        else:
            l = mid

    if r == len(ans):
        ans.append([now])
    else:
        ans[r].append(now)

print(len(ans))
for i in ans:
    print(len(i),*i)

