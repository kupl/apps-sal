n,k,q=map(int,input().split())
points=[0]*n
for _ in range(q):
    number=int(input())
    points[number-1]+=1
for i in points:
    if k-(q-i)<=0:
        print("No")
    else:
        print("Yes")
