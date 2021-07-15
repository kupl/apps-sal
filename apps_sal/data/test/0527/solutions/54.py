from bisect import bisect
s = list(input())
t = list(input())
lenT = len(t)
lenS = len(s)
alp = []

for i in range(26):
  array = []
  now = chr(ord('a') + i)
  for j in range(lenS):
    if s[j] == now:
      array.append(j)
  alp.append(array)

count,now = 0,-1

for i in range(lenT):
  j = ord(t[i])-ord('a')
  if alp[j]:
    next = bisect(alp[j],now)
    if next == len(alp[j]):
      count += 1
      now = alp[j][0]
    else:
      now = alp[j][next]
  else:
    print(-1)
    return

ans = count*lenS+now+1

print(ans)
