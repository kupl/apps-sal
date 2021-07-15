l=0
r=0
n=int(input())
for _ in range(n):
    x,y=[int(i) for i in input().split()]
    if x>0:
        l+=1
    if x<0:
        r+=1
if l<=1:
    print("Yes")
    return
if r<=1:
    print("Yes")
    return
print("No")

          

