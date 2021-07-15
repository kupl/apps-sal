n = int(input())
l = []
for i in range(n):
    w,h = map(int,input().split())
    l.append([w,h])
mx = max(l[0])
for i in range(1,n):
    if(max(l[i])<=mx):
        mx = max(l[i])
    elif(min(l[i])<=mx):
        mx = min(l[i])
    else:
        print('NO')
        return
print('YES')
