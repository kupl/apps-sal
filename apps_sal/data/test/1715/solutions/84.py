A, B, Q = map(int, input().split())
S = [-10**18]+sorted([int(input()) for _ in range(A)])+[10**18]
T = [-10**18]+sorted([int(input()) for _ in range(B)])+[10**18]
import bisect
for _ in range(Q):
  x = int(input())
  i = bisect.bisect_left(S, x)
  j = bisect.bisect_left(T, x)
  p, q, r, s = S[i-1], S[i], T[j-1], T[j]
  res = 10**18
  for a in (p, q):
    for b in (r, s):
      res = min(res, abs(x-a)+abs(a-b), abs(x-b)+abs(a-b))
  print(res)
