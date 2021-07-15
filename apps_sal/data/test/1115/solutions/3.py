R=lambda:list(map(int,input().strip().split()))
n=int(input())
a=R()
tot=sum(a)
m=int(input())
res=-1
for i in range(m):
    [l,r]=R()
    if r>=tot:
        res=max(l,tot)
        break
print(res)

