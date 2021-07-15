n=int(input())
a=[int(input()) for i in range(n)]
cnt=0
i=1
while i!=2:
    i=a[i-1]
    cnt+=1
    if cnt>10**5:
        cnt=-1
        break
print(cnt)

