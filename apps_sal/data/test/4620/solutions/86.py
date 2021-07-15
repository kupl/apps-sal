n=int(input())
num=[]
for i in range(n-1):
    num.append(list(map(int,input().split())))
for i in range(n-1):
    ans=0
    for j in range(i,n-1):
        if ans<=num[j][1]:
            ans=num[j][1]
        else:
            ans=num[j][1]+((-((ans-num[j][1])//-num[j][2]))*num[j][2])
        ans+=num[j][0]
    print(ans)
print((0))

