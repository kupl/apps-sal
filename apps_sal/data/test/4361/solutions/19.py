N, K = map(int,input().split())
H = []
min_dif = 1000000000000000000000000

for n in range(N):
  h = int(input())
  H.append(h)

H.sort()

for i in range(N-K+1):
  dif = H[i+K-1] - H[i]
  if dif < min_dif:
    min_dif = dif
    
print(min_dif)
