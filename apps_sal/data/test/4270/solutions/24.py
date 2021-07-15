#ABC138 C

N = int(input())
V = list(map(int,input().split()))
V.sort()
K = V[0]
for i in range(1,N):
    K = (K+V[i])/2
    
print(K)
