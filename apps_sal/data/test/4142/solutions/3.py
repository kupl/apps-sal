s=input()
check=True
for i in range(len(s)):
  if i%2==0 and s[i] not in ["R","U","D"]:
    check=False
  elif i%2==1 and s[i] not in ["L","U","D"]:
    check=False
print("Yes" if check else "No")
