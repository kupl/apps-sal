n=int(input())
s=list(map(int,input().split()))
su=0
a=[]
for i in range(n):
    su+=s[i]
    a.append(su)
for q in range(int(input())):
    l,r=map(int,input().split())
    if(l==1):
        print(a[r-1]//10)
    else:    
        print((a[r-1]-a[l-2])//10)
