a, b = map(int, input().split())

if a == 4 or a == 6 or a == 9 or a == 11:
  if b == 1 or b == 2 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
    print("No")
  else:
    print("Yes")
    
elif a == 2:
  print("No")
  
else:
  if b == 2 or b == 4 or b == 6 or b == 9 or b == 11:
    print("No")
  else:
    print("Yes")
