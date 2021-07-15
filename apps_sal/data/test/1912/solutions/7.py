mod=10**9+7
for _ in range (int(input())):
    r,g,b,w=map(int,input().split())
    ch=0
    if w%2==1 and r%2==g%2==b%2==0:
        ch=1
    elif w%2==0 and (r%2+g%2+b%2)<=1:
        ch=1
    if r>0 and g>0 and b>0:
        r-=1
        g-=1
        b-=1
        w+=3
    
    if w%2==1 and r%2==g%2==b%2==0:
        ch=1
    elif w%2==0 and (r%2+g%2+b%2)<=1:
        ch=1
    if ch==1:
        print("Yes")
    else:
        print("No")
