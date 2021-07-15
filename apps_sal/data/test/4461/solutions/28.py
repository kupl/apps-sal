h,w=map(int,input().split())
h_half=h//2
w_half=w//2
s_hw=h*w
min_x=s_hw

# H*n の範囲を探査
for n in reversed(range(1,w_half+2)):
  a=h*n
  b=h_half*(w-n)
  c=s_hw-(a+b)
  s1=max(a,b,c)-min(a,b,c)
  d=(w-n)//2*h
  e=s_hw-(a+d)
  s2=max(a,d,e)-min(a,d,e)
  min_x=min(min_x,s1,s2)

# n*W の範囲を探査
for n in reversed(range(1,h_half+2)):
  a=w*n
  b=w_half*(h-n)
  c=s_hw-(a+b)
  s1=max(a,b,c)-min(a,b,c)
  d=(h-n)//2*w
  e=s_hw-(a+d)
  s2=max(a,d,e)-min(a,d,e)
  min_x=min(min_x,s1,s2)

print(min_x)
