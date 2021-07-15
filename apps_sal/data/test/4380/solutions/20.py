A,B = map(int,input().split())
check = False
for C in range(1,4):
  if (A * B * C) % 2 == 1:
    check = True
    
print("Yes" if check else "No")
