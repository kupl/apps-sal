X,Y=map(int,input().split())

n=0
while X*2**n<=Y:
    n+=1

print(n)
