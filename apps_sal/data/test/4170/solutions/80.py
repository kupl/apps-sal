N = int(input())
H = list(map(int, input().split()))
 
ans, b = 0, 0
for i in range(N-1):
  if H[i] >= H[i+1]: b += 1
  else:
    ans = max(ans, b)
    b = 0
    
ans = max(ans, b)
print(ans)
