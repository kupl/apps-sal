def s(i):
    return sum([int(x) for x in str(i)])

x=[int(i) for i in input().split()]
a=x[0]
b=x[1]
c=x[2]
l=[]
for k in range(1,82):
    n=b*(k**a) +c
    if(n>0 and n<1000000000 and s(n)==k):
        l.append(n)
print(len(l))
for j in l:
    print(j,end=' ')
