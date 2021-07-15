N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if N <= K:
    print(N * X)
elif N >= K:
    k_stay = K * X
    k_plus_stay = (N - K) * Y
    print(k_plus_stay + k_stay)
