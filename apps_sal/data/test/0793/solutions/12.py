N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
mod = 10 ** 9 + 7
W = [1] * (N + 1)
for i, t in enumerate(T):
	W2 = W[:]
	k = 0
	for j, s in enumerate(S):
		if t == s:
			k += W[j]
		W2[j + 1] = (W[j + 1] + k) % mod
	W = W2
print(W[-1])
