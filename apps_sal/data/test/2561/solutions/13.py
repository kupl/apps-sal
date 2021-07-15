for i in range(int(input())):
    n=int(input())
    b=list(bin(n))[2:]
    ans=1
    for i in b:
        if i=='1':
            ans*=2
    print(ans)

