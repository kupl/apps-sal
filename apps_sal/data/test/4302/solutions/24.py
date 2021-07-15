a=list(map(int,input().split()))
a.sort()
r=a[-1]
a[-1]-=1
a.sort()
r+=a[-1]
print(r)
