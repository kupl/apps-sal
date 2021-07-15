N,K = map(int,input().split())
S = input()

# (K-1)文字目まで + K文字目 + K+1文字目から
print(S[:K-1] + S[K-1].lower() + S[K:])
