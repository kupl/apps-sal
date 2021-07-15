t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    odd,even=False,False
    for i in a:
        if i%2==0:
            even=True
        else:
            odd=True
        if odd and even:
            print('YES')
            break
    else:
        if odd and (not even) and n%2==1:
            print('YES')
        else:
            print('NO')

