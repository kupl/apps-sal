n = input()
sn = 0
for i in range(len(n)):
  sn += int(n[i])
print("Yes" if int(n)%sn == 0 else "No") 
