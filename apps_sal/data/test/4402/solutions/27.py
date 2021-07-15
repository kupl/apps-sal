a,b = map(int, input().split())

yen = 0
if a<= 5:
  yen = 0
elif a<=12:
  yen = b/2
else:
  yen = b
print(int(yen))
