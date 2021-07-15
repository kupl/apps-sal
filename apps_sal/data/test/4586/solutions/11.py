N = input()
check = False
for i in range(2):
  if N[i:i+3] == N[i] * 3:
    check = True
    
print("Yes" if check else "No")
