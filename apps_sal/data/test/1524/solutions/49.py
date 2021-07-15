s=list(input())
n =len(s)
ans=[1]*n
for i in range(n-1):
  if (s[i]=="R" and s[i+1] == "R"):
    ans[i+2]+=ans[i]
    ans[i]=0
for i in range(n-1,0,-1):
  if (s[i]=="L" and s[i-1] == "L"):
    ans[i-2]+=ans[i]
    ans[i]=0
print((" ".join(map(str,ans))))

