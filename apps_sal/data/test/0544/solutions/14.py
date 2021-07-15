cases=int(input())
for case in range(cases):
    n=int(input())
    s=list(input())
    can=True
    for i in range((n//2)+1):
        if not ((ord(s[i])+1==ord(s[n-1-i])-1) or (ord(s[i])-1==ord(s[n-1-i])+1) or ord(s[i])==ord(s[n-1-i])):
            can=False
            break
    if can:
        print("YES")
    else:
        print("NO")

