t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ans=0
    clockwiseflag=1
    antiflag=1
    for i in range(n):
        if s[i]=='>':
            antiflag=0
        if s[i]=='<':
            clockwiseflag=0
    if clockwiseflag or antiflag:
        print(n)
        continue
    for i in range(n):
        if (s[i]=='-' or s[(i+1)%n]=='-') :
            ans+=1
    print(ans)
