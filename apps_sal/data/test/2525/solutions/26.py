from collections import deque
S=deque()
S.extend(list(input()))
Q=int(input())
F=True

for _ in range(Q):
 q=input().split()
 if q[0]=='1':
   F=not(F)
 else:
   c=q[2]
   if (q[1]=='1' and F) or (q[1]=='2' and not(F)):
       S.appendleft(c)
   else:
       S.append(c)
print(''.join(list(S)) if F else ''.join(list(S)[::-1]))
