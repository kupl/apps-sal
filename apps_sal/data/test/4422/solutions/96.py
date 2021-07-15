N, K = map(int, input().split())
S = input()

s = S[K-1].lower()
print(S[:K-1] + s + S[K:])
