N,M = map(int,input().split())
yes = 100
no = 1900
ans = 0
for i in range(1,2**M+1):
  ans += (i*((M*no)+(N-M)*yes))/(i<<1)
print(int(ans)*2)
