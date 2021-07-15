r,c =list(map(int,input().split()))
op=[]
for i in range(r):
    ip=list(map(int,input().split()))
    op.append(min(ip))
print(max(op))
    

