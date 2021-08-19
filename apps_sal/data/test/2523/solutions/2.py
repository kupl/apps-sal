S = input()
L = len(S)
now = S[0]
ok = True
ans = 10 ** 18
for i in range(1, L):
    if S[i] != now:
        now = S[i]
        ans = min(ans, max(i, L - i))
        ok = False
if ok:
    print(L)
else:
    print(ans)
