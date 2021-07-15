import bisect
a,b,q = map(int, input().split())
s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
s.sort()
t.sort()
for i in range(q):
  ans = 10**11
  x = int(input())
  c = bisect.bisect_left(s,x)
  if c == 0:
    e1,e2 = s[0],s[0]
  elif c == a:
    e1,e2 = s[-1],s[-1]
  else:
    e1,e2 = s[c-1],s[c]
  f = bisect.bisect_left(t,e1)
  if f == 0:
    f1,f2 = t[0],t[0]
  elif f == b:
    f1,f2 = t[-1],t[-1]
  else:
    f1,f2 = t[f-1],t[f]
  ans = min(ans,abs(x-e1)+abs(e1-f1),abs(x-e1)+abs(e1-f2))
  f = bisect.bisect_left(t,e2)
  if f == 0:
    f1,f2 = t[0],t[0]
  elif f == b:
    f1,f2 = t[-1],t[-1]
  else:
    f1,f2 = t[f-1],t[f]
  ans = min(ans,abs(x-e2)+abs(e2-f1),abs(x-e2)+abs(e2-f2))
  d = bisect.bisect_left(t,x)
  if d == 0:
    f1,f2 = t[0],t[0]
  elif d == b:
    f1,f2 = t[-1],t[-1]
  else:
    f1,f2 = t[d-1],t[d]
  e = bisect.bisect_left(s,f1)
  if e == 0:
    e1,e2 = s[0],s[0]
  elif e == a:
    e1,e2 = s[-1],s[-1]
  else:
    e1,e2 = s[e-1],s[e]
  ans = min(ans,abs(x-f1)+abs(f1-e1),abs(x-f1)+abs(f1-e2))
  e = bisect.bisect_left(s,f2)
  if e == 0:
    e1,e2 = s[0],s[0]
  elif e == a:
    e1,e2 = s[-1],s[-1]
  else:
    e1,e2 = s[e-1],s[e]
  ans = min(ans,abs(x-f2)+abs(f2-e1),abs(x-f2)+abs(f2-e2))
  print (ans)
