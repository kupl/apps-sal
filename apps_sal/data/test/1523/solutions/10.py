from operator import itemgetter
n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
A=[]
B=[]
s=[]
max=0
sum=0
c=k-len(set(a))
if c==0:
    print(0)
else:
    for i in range(n):
        A.append((a[i],b[i]))
    B=sorted(A,key=itemgetter(0))
    max=B[0][1]
    for j in range(n-1):
        if B[j][0]==B[j+1][0]:
            if max<B[j+1][1]:
                s.append(max)
                max=B[j+1][1]
            else:
                s.append(B[j+1][1])
        else:
            max=B[j+1][1]
    s.sort()
    for k in range(c):
        sum+=s[k]
    print(sum)

