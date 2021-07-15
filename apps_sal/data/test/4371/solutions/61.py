s=input()
d=1000
for i in range(len(s)-1):
  if abs(int(s[i:i+3])-753)<d:
    d=abs(int(s[i:i+3])-753)
print(d)
