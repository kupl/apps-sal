(lambda N,M,K,n:print(N+sum(sorted(n[i+1]-n[i]-1for i in range(N-1))[:N-K])))(*map(int,input().split()),list(map(int,input().split())))
