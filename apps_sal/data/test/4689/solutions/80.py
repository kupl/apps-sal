K, N = map(int, input().split())
A = list(map(int, input().split()))

sub = [0] * (N - 1)

for i in range(N - 1):
	sub[i] = A[i + 1] - A[i]
sub.append(A[0] + (K - A[-1]))

print(sum(sub) - max(sub))
