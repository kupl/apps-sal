n=int(input())
a=[int(_) for _ in input().split()]
b=[int(_) for _ in input().split()]

d_a={}
d_b={}

for i in range(-1,n):
    d_a[i]=0
    d_b[i]=0

for i in range(n):
    d_a[a[i]-1]+=1
    d_b[b[i]-1]+=1

diff=0
c,d=0,0
for i in range(n):
    if d_a[i]+d_b[i]>n:
        print("No")
        return
    c+=d_a[i]
    d+=d_b[i-1]
    diff = max(diff,c-d)
print("Yes")
# for i in range(n):
#     print(a[i],end=" ")
# print()
for i in range(n):
    print(b[(i-diff)%n],end=" ")
print()
