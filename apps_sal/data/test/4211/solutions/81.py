n=int(input())
b=list(map(int,input().split()))
c=[b[0]]
for i in range(len(b)-1):
    x=min(b[i],b[i+1])
    c.append(x)
print(sum(c)+b[n-2])
