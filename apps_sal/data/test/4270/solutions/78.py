N = int(input())
v = list(map(int, input().split()))

v = sorted(v)
for i in range(N-1):
  v[i+1] = (v[i+1]+v[i])/2
  
print(v[N-1])
