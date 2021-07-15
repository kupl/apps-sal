n,x = list(map(int,input().split()))
l = list(map(int,input().split()))
a =[0]*(10**5+1)
b=[0]*(10**5+1)
count =0
flag=0
for i in range(n):
    if a[l[i]-1] == 0:
        a[l[i]-1] = 1
    else:
        count = 0
        flag=1
if flag == 0:
    for i in range(n):
        if a[(l[i]&x)-1] == 1 and l[i]&x != l[i]:
            count =1
            break
        else:
            if b[(l[i]&x)-1] == 1 :
                count =2
        b[(l[i]&x)-1] =1
if flag == 0 and count == 0:
    print('-1')
else:
    print(count)

