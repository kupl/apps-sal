from collections import Counter

n, p = map(int, input().split())
s = input()

ans = 0
if p == 2 or p == 5:
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += (i + 1)

else:
    mods = [0] * p
    mods[0] = 1
    m = 0
    d = 1
    for i in range(n):
        m = (m + int(s[-i - 1]) * d) % p
        d = (d * 10) % p
        mods[m] += 1

    for i in range(p):
        ans += mods[i] * (mods[i] - 1) // 2

print(ans)
