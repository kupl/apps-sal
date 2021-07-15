N = int(input())
W = list(map(int, input().split()))

# 累積和 => O(N)
S = [0] * N
S[0] = W[0]
for i in range(N-1):
  S[i+1] = S[i] + W[i+1]
  
# S[0] = W[0]
# S[1] = W[0] + W[1]
# S[2] = W[0] + W[1] + W[2]
# S[N-1] = W[0] + W[1] + ... + W[N-1]

# S[i] = W[0] + ... + W[i]
# S[N-1] - S[i] = W[i+1] + ... + W[N-1]

m = 10**10
for i in range(N-1):
  m = min(m, abs(S[N-1] - 2*S[i]))

print(m)
