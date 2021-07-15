s=str(input())
t=[]
t.append(s[0])
for i in range(1,len(s)):
  if s[i] in t:
    print("no")
    return
  t.append(s[i])

print("yes")
