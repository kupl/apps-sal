n=int(input())

syougen=[]
for i in range(n):
    a=int(input())
    
    for _ in range(a):
        x,y = list(map(int,input().split()))
        syougen.append([i,x-1,y])

ans = 0

for bit in range(2**n):
    
    for s in syougen:
        if (bit>>s[0])&1 == 1:
            if (bit>>s[1])&1 != s[2]:
                break
    else:
        thisans = str(bin(bit)).count("1")
        ans=max(ans,thisans)
        # print(bin(bit))
print(ans)

