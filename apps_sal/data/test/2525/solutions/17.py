from collections import deque
S = str(input());s = []
for i in range(len(S)):
  s.append(S[i])
s = deque(s)
Q = int(input())
eo = 0
for query in range(Q):
  temp = list(map(str,input().split()))
  if temp[0] == "1":
    eo += 1 #反転したということになる
  else:
    if temp[1] == "1":
      if eo%2 == 0:
        s.appendleft(temp[2])
      else:
        s.append(temp[2])
    else:
      if eo%2 == 0:
        s.append(temp[2])
      else:
        s.appendleft(temp[2])
#print(s)
s = list(s)
if eo%2 == 0:
  ans = "".join(s)
else:
  s = s[::-1]
  ans = "".join(s)
print(ans)
