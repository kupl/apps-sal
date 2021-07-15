n=int(input())
s=str(input())
ans = 0
t = ""
for i in range(n):
  t += s[i]
  if(len(t)>=3):
    if(t[-3:]=="fox"):
      t = t[0:-3]
      ans += 1
print(n-ans*3)
