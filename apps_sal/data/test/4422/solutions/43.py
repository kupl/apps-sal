(N, K) = map(int, input().split())
S = input()
print(S[:K - 1] + 'abc'[ord(S[K - 1]) - ord('A')] + S[K:])
