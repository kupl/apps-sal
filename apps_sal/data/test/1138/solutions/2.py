r,l,u,d = 0,0,0,0
for c in input():
    if(c=='R'):
        r += 1
    elif(c=='L'):
        l += 1
    elif(c=='U'):
        u += 1
    elif(c=='D'):
        d += 1
c = abs(r-l)+abs(u-d)
if(c%2==0):
    print(c//2)
else:
    print(-1)
