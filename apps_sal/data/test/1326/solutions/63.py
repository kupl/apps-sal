N= int(input())
ans = 0
for j in range(1,N+1):
  N_j = N//j
  ans += j*(1+N_j)*N_j//2
print(ans)
