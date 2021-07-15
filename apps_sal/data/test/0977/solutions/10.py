import bisect
def f(x):
    for i in range(n):
        z=bisect.bisect_right(li,x+i)
        if((z-i)%p==0):
            return 0
    return 1
l=input().split()
n=int(l[0])
p=int(l[1])
l=input().split()
li=[int(i) for i in l]
l=[]
li.sort()
for i in range(2001):
    if(f(i)):
        l.append(i)
print(len(l))
for i in l:
    print(i,end=" ")
