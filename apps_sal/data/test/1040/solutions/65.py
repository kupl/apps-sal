N=int(input())
s=input()

t="";
while len(s):
  t+=s[0]
  s=s[1:]
  if t[-3:]=="fox":
    t=t[:-3]
print(len(t))
