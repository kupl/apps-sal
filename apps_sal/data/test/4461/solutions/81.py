h, w = map(int, input().split())
if not h%3 or not w%3:
  print(0)
else:
  ans = min([h, w])
  for i in range(h):
    sub = max([abs(w*i-w//2*(h-i)), abs(w*i-(w-w//2)*(h-i))])
    if ans > sub:
      ans = sub
  for i in range(w):
    sub = max([abs(h*i-h//2*(w-i)), abs(h*i-(h-h//2)*(w-i))])
    if ans > sub:
      ans = sub
  print(ans)
