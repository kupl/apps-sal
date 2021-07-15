N,K=map(int,input().split())
if K == 0:
  answer = -N
else:
  answer = 0
for b in range(K+1,N+1):
  answer += N//b*(b-K)
  answer += max(0,N%b-K+1)
print(answer)
