N = int(input())
K = int(input())
x = list(map(int,input().split()))
distance = 0

for i in range(N):
  distance += min(2*x[i],2*abs(x[i]-K))
  
print(distance)
