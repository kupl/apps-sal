n=int(input())
s=[input() for _ in range(n)]
s.sort()
count=1
for i in range(n-1):
  if s[i]!=s[i+1]:
    count+=1
print(count)
