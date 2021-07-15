t=int(input())
for i in range(t):
    n=int(input())
    s=input().strip()
    o=0
    z=0
    for j in range(1,n):
        if s[j]==s[j-1]:
            if s[j]=='1':
                o=o+1
            else:
                z=z+1
    print(max(z,o))
