N,K = map(int,input().split())
K = abs(K)
print(sum((N-abs(N-n))*(N-abs(N-n+K)) for n in range(K+1,2*N)))
