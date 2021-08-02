s = int(input())
t = 1 if s >= 3 else 0
m = 10**9 + 7
S = [1] + [0] * 2000

for i in range(1, 2000):
    S[i] = S[i - 1] * i

for i in range(2, s // 3 + 1):
    t = (t + S[s - 2 * i - 1] // S[i - 1] // S[s - 3 * i]) % m

print(t)
