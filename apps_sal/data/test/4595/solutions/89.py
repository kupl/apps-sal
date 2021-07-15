s=str(input())
for i in range(len(s)):
  if s[i]=="A":
    a=i
    break
t=s[::-1]
for j in range(len(s)):
  if t[j]=="Z":
    b=j
    break

print(len(s)-a-b)
