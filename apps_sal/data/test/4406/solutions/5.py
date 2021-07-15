n,k=map(int,input().split())
ide=input().split()
for i in range(n):
    ide[i]=int(ide[i])
a=[]
for i in range(n):
    if(ide[i] in a):
        continue
    else:
        if(len(a)<k):
            a.append(ide[i])
        else:
            a.pop(0)
            a.append(ide[i])
print(len(a))
for i in range(len(a)):
    print(a[len(a)-1-i],end=" ")
print()    
