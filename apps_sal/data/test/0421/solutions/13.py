a=int(input())
b=[]
total=0
for i in range(a):
    x,y=list(map(int,input().split()))
    b.append([x,y])
b.sort(key=lambda x: x[1])
ending=0
for i in b:
    if i[0]>ending:
        total+=1
        ending=i[1]
print(total)

