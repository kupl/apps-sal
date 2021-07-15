res = 0
n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if cnt==3:
        res+=1
        cnt = 0
    if a[i]>3:
        cnt+=1
    else:cnt = 0
if cnt==3:
    res+=1
print(res)
