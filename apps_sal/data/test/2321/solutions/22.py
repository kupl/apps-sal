for _ in range(int(input())):
    n=int(input())
    s=list(input())
    x,y=-1,-1
    for i in range(n):
        if s[i]=='>':
            x=i
            break
    for i in range(n-1,-1,-1):
        if s[i]=='<':
            y=n-1-i
            break
    if x==-1 or y==-1:
        print(0)
    else:
        print(min(x,y))
