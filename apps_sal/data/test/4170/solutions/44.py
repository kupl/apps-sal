N = int(input())
H = list(map(int, input().split()))

a = 0
ans = 0
for i in range(N-1):
  if H[i] >= H[i+1]: a += 1
  else: 
    a = 0
  ans = max(ans, a)
print(ans)
