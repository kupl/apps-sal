N, K = map(int, input().split())
S = input()
 
if S[K-1] == 'A': rep = 'a'
elif S[K-1] == 'B': rep = 'b'
else: rep = 'c'

# (K-1)文字目まで + K文字目 + K+1文字目から
print(S[:K-1] + rep + S[K:])
