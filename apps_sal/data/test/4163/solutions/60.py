n=int(input())
c=0
for i in range(n):
    d1,d2 = map(int,input().split())
    if d1 == d2:
        c+=1
    else:
        c=0
    
    if c==3:
        print('Yes')
        break
else:
    print('No')
