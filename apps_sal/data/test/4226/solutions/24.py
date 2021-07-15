x,y=map(int,input().split())
ans=0
for i in range(x+1):
    j=x-i
    if 2*i+4*j==y:
        ans=1
print('Yes'if ans else'No')
