n = int(input())
b = list(map(int,input().split()))
c=0
for i in range(len(b)-1):
    c+=min(b[i],b[i+1])
print(c+b[0]+b[-1])
