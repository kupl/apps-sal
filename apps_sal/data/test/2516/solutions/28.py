from collections import Counter
N, MOD = map(int, input().split())
S = input()
res = 0
if MOD == 2 or MOD == 5:
    for i in range(N):
        if(int(S[N - i - 1]) % MOD == 0):
            res += N - i
else:
    Cum = [0] * (N + 1)
    for i in range(N):
        Cum[i + 1] = (Cum[i] + int(S[N - i - 1]) * pow(10, i, MOD)) % MOD
    c = Counter(Cum).most_common()
    for a, b in c:
        res += b * (b - 1) // 2
print(res)
