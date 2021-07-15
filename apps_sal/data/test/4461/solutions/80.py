h, w = map(int, input().split())

ans = 10**9
for i in range(1,h):
  x = h-i
  s0 = i*w
  s1 = x*(w//2)
  s2 = x*(w-w//2)
  s = max(s0,s1,s2)-min(s0,s1,s2)
  ans = min(ans,s)
  s3 = w*(x//2)
  s4 = w*(x-x//2)
  s = max(s0,s3,s4)-min(s0,s3,s4)
  ans = min(ans,s)

for i in range(1,w):
  x = w-i
  s0 = i*h
  s1 = x*(h//2)
  s2 = x*(h-h//2)
  s = max(s0,s1,s2)-min(s0,s1,s2)
  ans = min(ans,s)
  s3 = h*(x//2)
  s4 = h*(x-x//2)
  s = max(s0,s3,s4)-min(s0,s3,s4)
  ans = min(ans, s)
print(ans)
