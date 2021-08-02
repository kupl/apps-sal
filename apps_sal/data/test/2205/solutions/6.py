t, maxn = [0], 1000005
for i in range(1, maxn):
    t.append(t[-1] ^ i)
n, res = int(input()), 0
v = [int(i) for i in input().split()]
for i in v:
    res ^= i
for i in range(1, n + 1):
    if (n // i) % 2 == 1:
        res = res ^ (t[i - 1]) ^ (t[n % i])
    else: res ^= t[n % i]
print(res)
