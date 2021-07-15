n,m,d=[int(x) for x in input().split(' ')]
list1=[int(x) for x in input().split(' ')]
x=(m+1)*(d-1)+sum(list1)
list2=[]
a=0
b=0
if x < n:
    print('NO')
else:
    print('YES')
    n0=n-sum(list1)
    while b <= m:
        if a == 0:
            if n0 >= d-1:
                list2.extend(['0']*(d-1))
                a+=1
                b+=1
                n0-=(d-1)
            elif 0 < n0 < (d-1):
                list2.extend(['0']*n0)
                a+=1
                b+=1
                n0=0
            else:
                a+=1
                b+=1
        else:
            list2.extend([str(b)]*list1[b-1])
            a-=1
    print(' '.join(list2)) 
        
    

