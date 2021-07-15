M=99999999999983
def Hash(s):
    h=0
    p=1
    for c in s:
        h=(h+p*(ord(c)-94))%M
        p=(p*17)%M
    return h
n,m=list(map(int,input().split()))
a=set()
for i in range(n):
    s=input()
    h=Hash(s)
    p=1
    for j in range(len(s)):
       for k in range(97,100):
           if ord(s[j])!=k:
               a.add((h+p*(k-ord(s[j])))%M)
       p=(p*17)%M
ans=[]
for i in range(m):
    s=input()
    b=Hash(s)
    if b in a:
        ans.append('YES')
    else:
        ans.append('NO')
print('\n'.join(ans))

