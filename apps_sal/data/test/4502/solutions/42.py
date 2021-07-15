from collections import deque
n=int(input())
a=[int(x) for x in input().rstrip().split()]

ans=deque()
for i in range(n):
  if (i+1)%2==1:
    ans.appendleft(str(a[i]))
  else:
    ans.append(str(a[i]))

ans=list(ans)
if n%2==0:
  print((*ans[::-1]))
else:
  print((*ans))

