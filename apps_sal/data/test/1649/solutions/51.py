s = list(map(int,input().split()))

for i in range(2**4):
    total=sum(s)
    ans=0
    for j in range(4):
        if i>>j&1:
            ans+=s[j]
            total-=s[j]
            if ans==total:
                print("Yes")
                return

print("No")
