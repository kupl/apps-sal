N = int(input())
W = list(map(int, input().split()))

S = [0] * N
S[0] = W[0]
for i in range(N - 1):
    S[i + 1] = S[i] + W[i + 1]


m = 10**10
for i in range(N - 1):
    m = min(m, abs(S[N - 1] - 2 * S[i]))

print(m)
