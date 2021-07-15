N,*P=map(int,open(0).read().split())
S='YES' if sum([P[i]==i+1 for i in range(N)])>=N-2 else 'NO'
print(S)
