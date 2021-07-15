N = int(input())
L = list(map(int, input().split()))
L = sorted(L)
ans = 0
for i in range(N):
  ans += L[2 * i]
  
print(ans)  
