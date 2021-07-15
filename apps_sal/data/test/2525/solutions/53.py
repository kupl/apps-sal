from collections import deque
s = deque(list(input()))
n = int(input())
normal = 0
for i in range(n):
  li = input().split()
  if int(li[0]) == 1:
    normal ^= 1
  else:
    k = int(li[1]) - 1
    k ^= normal
    if k == 1:
      s.append(li[2])
    else:
      s.appendleft(li[2])
print(''.join(s) if normal == 0 else ''.join(list(s)[::-1]))      
