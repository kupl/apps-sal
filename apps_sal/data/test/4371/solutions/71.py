s=[int(i) for i in input()]
ans=1000
for i in range(2,len(s)):
  tmp=s[i-2]*100+s[i-1]*10+s[i]
  ans=min(ans,abs(753-tmp))
print(ans)
