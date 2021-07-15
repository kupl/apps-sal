N,X,mod=map(int,input().split())
l=[X]
se=set(l)
mem=-1
for i in range(N-1):
   if l[-1]**2%mod in se:
      mem=l[-1]**2%mod
      break
   else:
      c=l[-1]**2%mod
      l.append(c);se.add(c)
if mem==-1:
   print(sum(l))
   return
N-=i+2
ans=sum(l)
index=l.index(mem)
roop=len(l)-index
l=l[index:]
can,rem=divmod(N,roop)
ans+=sum(l)*can
ans+=sum(l[:rem+1])
print(ans)
