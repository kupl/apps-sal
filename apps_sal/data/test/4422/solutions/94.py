N,K=list(map(int, input().split()))
S=input().strip()
c=S[K-1].lower()
print((S[:K-1]+c+S[K:]))


