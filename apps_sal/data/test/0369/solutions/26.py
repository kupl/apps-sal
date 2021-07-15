n,m=map(int,input().split())
s=input()[::-1]
ans=[]
pos=0
while pos!=n:
  for i in range(min(n-pos,m),0,-1):
    if s[pos+i]=='0':
      ans.append(i)
      pos+=i
      break
  else:
    print(-1)
    return
print(*ans[::-1])
