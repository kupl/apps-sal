N, K = list(map(int, input().split()))
S = input()
print((S[0:K - 1] + S[K - 1].lower() + S[K:N]))
