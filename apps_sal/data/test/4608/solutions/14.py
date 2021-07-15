n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
total=1
i=a[0]-1
if a[0]==2:
    print(total)
else:
    while True:
        if a[i]==2:
            print(total+1)
            break
        elif total>n:
            print("-1")
            break
        else:
            i=a[i]-1
            total+=1
