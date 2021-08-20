MOD = 10 ** 9 + 7
S = input()
cur = [0] * 13
cur[0] = 1
r = 1
base = 0
for i in range(len(S)):
    s = S[-(i + 1)]
    if s == '?':
        prev = cur
        cur = [sum(prev)] * 13
        for m in range(13):
            for d in range(10, 13):
                cur[(m + r * d) % 13] -= prev[m]
        for m in range(13):
            cur[m] %= MOD
    else:
        base = (base + r * int(s)) % 13
    r = 10 * r % 13
print(cur[(5 - base) % 13])
