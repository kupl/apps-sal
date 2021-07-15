w,a,b = map(int,input().split())
#print(w,a,b)
if a+w < b:
  print(abs(b-(a+w)))
elif b+w < a:
  print(abs(a-(b+w)))
else:
  print(0)
