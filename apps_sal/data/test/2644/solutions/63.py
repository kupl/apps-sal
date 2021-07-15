n = int(input())
p = [int(x)-1 for x in input().split()]
ans, used = [],[False]*n
for i in range(n):
    while i > 0 and  p[i-1]>p[i]:
        if used[i]:
            print(-1)
            return
        else:
            used[i] = True
            p[i-1],p[i] = p[i],p[i-1]
            ans.append(i)
            i -= 1
if len(ans)==n-1:
    print(*ans,sep="\n")
else:
    print(-1)
