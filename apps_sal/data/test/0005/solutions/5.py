n,pos,l,r = list(map(int,input().split()))
if (pos > r):
    if (l == 1):
        print(pos-r+1)
    else:
        print(pos-l+2)
elif(pos < l):
    if (r == n):
        print(l-pos+1)
    else:
        print(r-pos+2)
else:
    if (l == 1 and r == n):
        print(0)
    elif l == 1:
        print(r-pos+1)
    elif r == n:
        print(pos-l+1)
    else:
        print(r-l + min(pos-l, r-pos) + 2)
    

