n=int(input())//2
a=list(map(int,input().split(' ')))
b=[0]*n
a.reverse()
for i in a:
    b.append(i)
mem=b[-1]
c=0
for i in range(n-1):
    if b[-2-i]-c>mem:
        c=b[-2-i]-mem
    b[-2-i]-=c
    b[1+i]+=c
    mem=b[-2-i]
for i in b:
    print(i,end=' ')

