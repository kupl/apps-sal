N = int(input())
b = list(map(int,input().split()))
a = [0]*(N)
a[0] = b[0]
a[N-1] = b[N-2]
for i in range(N-2):
  a[i+1] = min(b[i],b[i+1])
  
print(sum(a))
