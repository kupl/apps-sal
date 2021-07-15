abcde=[int(input()) for i in range(5)]
ans=0
m=10
for i in abcde:
  ans += (i+9)//10*10
  m=min(m,(i-1)%10+1)
print(ans-10+m)
