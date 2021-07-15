n,m = list(map(int,input().split()))
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

flag = False
for i in range(n-m+1):

    for s in range(n-m+1):
        if b[0]==a[i][s:s+m]:
            index = s
            cnt = 1
            for j in range(1,m):
                if not a[i+j][index:index+m]==b[j]:
                    break
                cnt+=1
            if cnt==m:
                flag = True
                break


print(("Yes" if flag else "No"))

