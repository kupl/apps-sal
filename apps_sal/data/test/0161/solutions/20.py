n=int(input())
a=[]
i=30
if not n&1:
    a.append(0)
    n^=1
while 2**i>n:
    i-=1
while i>1:
    if not (n&(2**(i-1))):
        a.append(i)
        n^=(2**i)-1
        n+=1
    i-=1
print(2*len(a))
for num in a:
    print(str(num),end=" ")

