A,B,X = map(int, input().split())

if A*10**9+B*10 < X:
  print(10**9)
elif A*1+B*1 > X:
  print(0)
else:
  min_val = 1
  max_val = 10**9
  tmp = (min_val+max_val)//2
  prev_price = 0
  
  while 1:
    price = A*tmp + B*len(str(tmp))
    if price == prev_price:
      print(tmp)
      break
    
    if price < X:
      min_val = tmp
      tmp = (min_val+max_val)//2
    elif price > X:
      max_val = tmp
      tmp = (min_val+max_val)//2
    else:
      print(tmp)
      break
    prev_price = price
