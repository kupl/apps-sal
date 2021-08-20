(N, M, K) = list(map(int, input().split()))
P = 998244353
(t, c) = (M * pow(~-M, ~-N, P), 1)
for k in range(1, K + 1):
    c = c * (N - k) * pow(k, P - 2, P) % P
    t = (t + M * c * pow(~-M, ~-N - k, P)) % P
print(t % P)
