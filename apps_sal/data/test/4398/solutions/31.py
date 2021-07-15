N = int(input())

a, b = input().split()

ans = ''

for i in range(N):
  ans += a[i] + b[i]
  
print(ans)

