
def ri():
    return map(int, input().split())


n, k = ri()

s = list(ri())
sd = dict()
for i in range(1, n):
    s[i] = s[i] + s[i - 1]

s.append(0)

ans = 0
pows = set([k**i for i in range(50)])
for i in range(n - 1, -1, -1):
    if not s[i] in sd:
        sd[s[i]] = 1
    else:
        sd[s[i]] += 1
    for pow in pows:
        p = pow + s[i - 1]
        if p in sd:
            ans += sd[p]
print(ans)
