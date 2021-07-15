N = int(input())
V = sorted(list(map(int,input().split())))
ans = (V[0]+V[1])/2

for n in range(2,N):
  ans = (ans+V[n])/2
  
print(ans)
