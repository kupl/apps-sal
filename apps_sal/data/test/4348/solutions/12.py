n,k = list(map(int, input().split() ) )
s=input()
alph=[chr(ord('a')+i) for i in range(26)]
for a in alph:
    if k==0:
        break
    if s.count(a)<=k:
        k-=s.count(a)
        s=s.replace(a,'')
    else:
        s=s.replace(a,'', k)
        k=0
print(s)
