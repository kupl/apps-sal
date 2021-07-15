N, P = list(map(int, input().split()))
S = input()
from collections import Counter
ans = 0
if P == 2 or P == 5:
    for i in range(N-1, -1, -1):
        t = S[i]
        if not int(t) % P:
            ans += i + 1
else:
    c = Counter()
    c[0] += 1
    p = 1
    t = int(S[N-1])
    c[t%P] += 1
    for i in range(N-2, -1, -1):
        p *= 10
        t = int(S[i]) * p + t
        c[t % P] += 1
        p %= P
    for a in list(c.values()):
        ans += (a * (a-1)) // 2
print(ans)

