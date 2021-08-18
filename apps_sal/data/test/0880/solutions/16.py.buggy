MOD = 998244353
def I(): return list(map(int, input().split()))


n, = I()

s = [1, 2]
for i in range(3, 10**6 + 1):
    s.append(((s[-1] + 1) * i) % MOD)

f = 1
l = []
for i in range(1, 10**6 + 1):
    l.append((f * i) % MOD)
    f = (f * (i + 1)) % MOD
    # print(f)
# print(l)
# print(s)
n -= 1
if n == 0:
    print(1)
    return
print((l[n] - s[n]) % MOD)
# print()
