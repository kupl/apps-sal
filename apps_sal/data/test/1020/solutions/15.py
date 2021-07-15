w,h,k=list(map(int,input().split()))
s=0
for i in range(k):
    s+=w*2+(h-2)*2
    w-=4
    h-=4
print(s)

