
N, K = list(map(int, input().split()))

cand1 = N % K
cand2 = K - cand1
print((min(N, cand1, cand2)))
