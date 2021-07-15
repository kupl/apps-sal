n=int(input())
s,t=input().split()
new=""
for i in range(n):
  new+=s[i]
  new+=t[i]
print(new)
