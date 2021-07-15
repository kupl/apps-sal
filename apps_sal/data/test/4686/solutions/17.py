w = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

check = True
for a in alpha:
  if w.count(a) % 2 == 1:
    check = False
    
print("Yes" if check else "No")
