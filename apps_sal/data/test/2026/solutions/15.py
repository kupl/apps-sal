n=int(input())
s=input()
s=list(s)
r,l,u,d=0,0,0,0
points=0
for i in s:
    if(i=='R'):
        r=1
        if(l==1):
            points+=1
            l, u, d = 0, 0, 0
    if (i == 'L'):
        l = 1
        if (r == 1):
            points += 1
            r, u, d = 0, 0, 0
    if (i == 'U'):
        u = 1
        if (d == 1):
            points += 1
            l, r, d = 0, 0, 0

    if (i == 'D'):
        d = 1
        if (u == 1):
            points += 1
            l, u, r = 0, 0, 0
print(points+1)
