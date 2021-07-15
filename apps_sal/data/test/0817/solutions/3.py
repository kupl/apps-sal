import sys
z=sys.stdin.readline
s=z().strip()
l=len(s)
b=[' ']
o=[]
m=[' ']
for i in range(l):
 c=s[-1-i]
 if c==b[-1]:
  if c>m[-1].lower() or (c==m[-1].lower() and c>m[-2].lower()):
   b.pop()
   if b[-1].lower()!=m[-1].lower():m.pop()
   b[-1]=b[-1].upper()
   m[-1]=m[-1].upper()
  else:b+=[c]
 else:
  b+=[c]
  if b[-1]!=m[-1].lower():m+=[b[-1]]
 if len(b)>11:o+=[(str(len(b)-1)+' '+''.join(b[:-6:-1])+'...'+b[2]+b[1]).lower()]
 elif len(b)>1:o+=[(str(len(b)-1)+' '+''.join(b[-1::-1])).lower()]
 else:o.append('0')
print('\n'.join(o[::-1]))
