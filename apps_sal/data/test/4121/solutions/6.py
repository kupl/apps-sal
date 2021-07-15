i,p=input,print;n,b,q=int(i()),[int(x)&1 for x in i().split()],[];f=q.append;f(b[0])
for a in b[1:]:q.pop() if q and q[-1] == a else f(a)
p('NO'if len(q)>1 else'YES')
