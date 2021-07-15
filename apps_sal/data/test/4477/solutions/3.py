rn=lambda:int(input())
rl=lambda:list(map(int,input().split()))
rns=lambda:map(int,input().split())
rs=lambda:input()
yn=lambda x:print('Yes') if x else print('No')
YN=lambda x:print('YES') if x else print('NO')

for _ in range(rn()):
    x=rs()
    n=int(x[0])
    ans=10*(n-1)
    for i in range(len(x)+1):
        ans+=i
    print(ans)

