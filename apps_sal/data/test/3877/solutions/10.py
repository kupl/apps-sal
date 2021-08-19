(N, L, R) = map(int, input().split())
S = ''
while N > 0:
    S = str(N % 2) + S
    N //= 2
RAns = 0
for i in range(1, len(S) + 1):
    if R >= 2 ** (i - 1):
        RAns += 1 * int(S[i - 1])
        RAns += (R - 2 ** (i - 1)) // 2 ** i * int(S[i - 1])
L -= 1
LAns = 0
for i in range(1, len(S) + 1):
    if L >= 2 ** (i - 1):
        LAns += 1 * int(S[i - 1])
        LAns += (L - 2 ** (i - 1)) // 2 ** i * int(S[i - 1])
print(RAns - LAns)
