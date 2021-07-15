n=int(input())
p=[int(x) for x in input().split()]
s=0
for i in p:
    if i<=0:
        s+=1
if n%2==0 and s%2!=0:
    q = 1000
    for i in p:
        if  abs(i) <= q:
            q = abs(i)
    print(sum(abs(i) for i in p) - 2 * q)

else:
        print(sum(abs(i) for i in p))








