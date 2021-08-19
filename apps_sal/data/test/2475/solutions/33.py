N = int(input())
S = [int(a) for a in input().split()]
ma = 0
for C in range(1, N - 1):
    s = 0
    for k in range((N - 2) // C):
        A = N - 1 - k * C
        if A % C == 0 and A // C <= k:
            continue
        s += S[k * C] + S[-1 - k * C]
        ma = max(ma, s)
print(ma)
