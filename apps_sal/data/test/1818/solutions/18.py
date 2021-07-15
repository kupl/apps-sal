n=int(input())
l=[int(i) for i in input().split()]
def cnt(n):
    c=0 
    while n:
        if n&1:
            c=c+1 
        n=n//2 
    return c 
bits=[0]*40 
for i in l:
    bits[cnt(i)]+=1 
ans=0 
for i in range(40):
    ans=ans+(bits[i]*(bits[i]-1)//2)
print(ans)
