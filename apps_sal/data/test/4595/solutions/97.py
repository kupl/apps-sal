s = input()
n = len(s)

for i in range(n-1):
  if s[i] == "A":
    break
    
for j in range(1,n)[::-1]:
  if s[j] == "Z":
    break
    
print(len(s[i:j+1]))
