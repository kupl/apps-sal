N = int(input())
H = list(map(int,input().split()))

V = sum(H)
E = 0

for i in range(1,N):
  E += min(H[i-1],H[i])
  
print(V-E)
