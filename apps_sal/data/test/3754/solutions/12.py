N = int(input())
D = list(map(int, input().split()))
mod = 998244353

ANS = 1
S = 0
for d in D:
    ANS = ANS * d % mod
    S += d

for i in range(N - 2):
    ANS = ANS * (S - N - i) % mod

print(ANS)
