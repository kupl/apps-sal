a,b=map(int,input().split())
c,d=map(int,input().split())
s={b-d}
while b!=d:
    if b<d: b+=a
    else: d+=c
    bd=b-d
    if bd in s: break
    s|={bd}
if d==b: print(b)
else: print(-1)
