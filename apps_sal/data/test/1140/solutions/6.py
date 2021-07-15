n=int(input())
b=[int(i) for i in input().split()]
mi=min(b)
ma=max(b)
a1=ma-mi
if(a1==0):
    a2=len(b)*(len(b)-1)//2
else :
    a2 = b.count(mi)*b.count(ma)
print(a1,a2)

