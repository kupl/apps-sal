[n,m]=[int(i) for i in input().split()]
v=set()
M=9999999999999983
for i in range(n):
    s=input()
    l=len(s)
    [haf,hb]=[0,1]
    for j in range(l):
        haf=(haf+hb*ord(s[j]))%M
        hb=(hb*131)%M
    hb=1
    for k in range(l):
        for j in range(97,100):
            if ord(s[k])!=j:
                v.add((haf+hb*(j-ord(s[k])))%M)
        hb=(hb*131)%M
ans=[]
for i in range(m):
    s=input()
    hb=1
    haf=0
    for j in range(len(s)):
        haf=(haf+hb*ord(s[j]))%M
        hb=(hb*131)%M
    ans.append('YES' if haf in v else 'NO')
print('\n'.join(ans))
