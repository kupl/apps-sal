h,w=map(int,input().split())
min_ = h*w
if h % 3 == 0:
  min_ = 0
else:
  min_ = min(min_, w)
if w % 3 == 0:
  min_ = 0
else:
  min_ = min(min_, h)
for i in range(1, w):
  p1 = h//2*i
  p2 = (h-h//2)*i
  p3 = h*(w-i)
  min_ = min(min_, max(p1,p2,p3)-min(p1,p2,p3))
for i in range(1, h):
  p1 = w//2*i
  p2 = (w-w//2)*i
  p3 = w*(h-i)
  min_ = min(min_, max(p1,p2,p3)-min(p1,p2,p3))
print(min_)
