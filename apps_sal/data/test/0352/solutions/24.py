n=int(input())
min1,max1=map(int,input().split())
min2,max2=map(int,input().split())
min3,max3=map(int,input().split())
ans1=min1
ans2=min2
ans3=min3
n-=min1+min2+min3
max1=max1-min1
max2=max2-min2
max3=max3-min3
while n>0:
    if max1>0:
        if max1>=n:
            ans1+=n
            max1-=n
            n=0
        else:
            n=n-max1
            ans1+=max1
            max1=0
    elif max2>0:
         if max2>=n:
            ans2+=n
            max2-=n
            n=0
         else:
            n=n-max2
            ans2+=max2
            max2=0
    elif max3>0:
         if max3>=n:
            ans3+=n
            max3-=n
            n=0
         else:
            n=n-max3
            ans3+=max3
            max3=0
print(ans1,ans2,ans3)
