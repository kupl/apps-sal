from bisect import bisect_left

S = input()
T = input()

ss = set(list(S))
st = set(list(T))
if not (st <= ss):
    print((-1))
    return
alpha = {chr(97 + i): [] for i in range(26)}
for i, s in enumerate(S):
    alpha[s].append(i + 1)
n = len(S)
now = 0
ans = 0
for t in T:
    if alpha[t][-1] <= now:
        ans += (n - now) + alpha[t][0]
        now = alpha[t][0]
    else:
        i = bisect_left(alpha[t], now + 1)
        ans += alpha[t][i] - now
        now = alpha[t][i]
print(ans)
