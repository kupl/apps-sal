n,k=[int(x) for x in input().split()]
a=(n-k)//2
tot=''
for i in range(n):
    if (i+1)%(a+1)==0:
        tot+='1'
    else:
        tot+='0'
print(tot)

