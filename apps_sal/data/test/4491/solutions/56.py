n=int(input())
a = [list(map(int,input().split())) for _ in range(2)]

amemax=0
for i in range(n):
    ame=sum(a[0][:i+1])+sum(a[1][i:])
    amemax = max(ame,amemax)
    
print(amemax)
