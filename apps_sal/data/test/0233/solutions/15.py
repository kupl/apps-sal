n=int(input())
m=0
c=0
for i in range(n):
    m1,c1=map(int,input().split())
    if m1>c1:
        m+=1
    elif m1<c1:
        c+=1
if m>c:
    print("Mishka")
elif m<c:
    print("Chris")
else:
    print("Friendship is magic!^^")
