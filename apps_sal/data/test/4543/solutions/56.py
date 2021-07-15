import math
ab=list(input().split())
s=int(''.join(ab))

root=int(math.sqrt(s))
if root*root==s: print('Yes')
else: print('No')
