N, P = map(int, input().split())
S = input()

mods = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    mods[i] = (int(S[i]) * pow(10, N - i - 1, P) + mods[i + 1]) % P
c = dict()
for m in mods:
    c[m] = c.get(m, 0) + 1

ans = 0
if P == 2 or P == 5:
    for i, s in enumerate(S):
        s = int(s)
        if s % P == 0:
            ans += i + 1
else:
    for i in range(N):
        c[mods[i]] -= 1
        ans += c[mods[i]]

print(ans)
