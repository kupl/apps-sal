N = int(input())
A = list(map(int, input().split()))
 
l = [0]*N
for i in range(N):
  l[A[i]-1] = str(i+1)

ans = ''
for i in range(N):
  ans += (l[i] + ' ')
  
print(ans)
