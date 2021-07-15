import bisect
a,b,q = map(int, input().split())
INF = 10**18
s = [int(input()) for i in range(a)]
s = [-INF] + s + [INF]
t = [int(input()) for i in range(b)]
t = [-INF] + t + [INF]
s.sort()
t.sort()
for i in range(q):
  ans = 10**11
  x = int(input())
  c = bisect.bisect_left(s,x)
  e1,e2 = s[c-1],s[c]
  f = bisect.bisect_left(t,e1)
  f1,f2 = t[f-1],t[f]
  ans = min(ans,abs(x-e1)+abs(e1-f1),abs(x-e1)+abs(e1-f2))
  f = bisect.bisect_left(t,e2)
  f1,f2 = t[f-1],t[f]
  ans = min(ans,abs(x-e2)+abs(e2-f1),abs(x-e2)+abs(e2-f2))
  d = bisect.bisect_left(t,x)
  f1,f2 = t[d-1],t[d]
  e = bisect.bisect_left(s,f1)
  e1,e2 = s[e-1],s[e]
  ans = min(ans,abs(x-f1)+abs(f1-e1),abs(x-f1)+abs(f1-e2))
  e = bisect.bisect_left(s,f2)
  e1,e2 = s[e-1],s[e]
  ans = min(ans,abs(x-f2)+abs(f2-e1),abs(x-f2)+abs(f2-e2))
  print (ans)
