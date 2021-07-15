tests = int (input())
for test in range (tests):
  n, x, m = map (int, input().split())
  l, r = x, x
  for i in range (m):
    ln, rn = map (int, input().split())
    if ln <= r and rn >= l:
      l = min (l, ln)
      r = max (r, rn)
  print (r - l + 1) 
