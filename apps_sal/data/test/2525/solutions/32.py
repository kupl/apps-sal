from collections import deque
S=deque()
S.extend(list(input()))
F=True

for _ in range(int(input())):
 p,*q=input().split()
 if p=='1':F=not(F)
 else:
   c=q[1]
   if (q[0]=='1' and F) or (q[0]=='2' and not(F)):S.appendleft(c)
   else:S.append(c)
print(''.join(list(S) if F else list(S)[::-1]))
