h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

ans = []
for i, ai in enumerate(a):
  ans.extend([str(i+1)] * ai)
  
for i in range(h):
  l = ans[i * w : (i + 1) * w ]
  if i % 2:
    l.reverse()
  print(' '.join(l))
