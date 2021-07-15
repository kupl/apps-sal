n,k=map(int,input().split())
h=[int(input()) for _ in range(n)]

h.sort()
result = 10**9
for i in range(n-k+1):
  result = min(result, h[i+k-1] - h[i])

print(result)
