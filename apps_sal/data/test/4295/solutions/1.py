(N, K) = map(int, input().split())
s = N // K
s1 = abs(N - K * s)
s2 = abs(N - K * (s + 1))
print(min(s1, s2))
