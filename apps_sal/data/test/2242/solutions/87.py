from collections import Counter
S = input()
P = [0] * (len(S) + 1)
mod = 2019
d = 1
for i in range(len(S), 0, -1):
    P[i - 1] = int(S[i - 1]) * d + P[i]
    P[i - 1] = P[i - 1] % mod
    d *= 10
    d = d % mod
P = Counter(P)
ans = 0
for p in P.values():
    ans += p * (p - 1) // 2
print(ans)
