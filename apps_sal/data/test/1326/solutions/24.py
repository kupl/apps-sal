n = int(input())
ans = 0
for i in range(1,n+1):
  temp = n // i
  ans += (temp * i * (temp + 1))//2
print(ans)
