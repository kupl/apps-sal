from random import randint
n = int(input())
a = list(map(int, input().split()))
a += a
b = list(map(int, input().split()))
aa = [a[i - 1] ^ a[i] for i in range(1, n * 2)]
bb = [b[i - 1] ^ b[i] for i in range(1, n)]
s = bb + aa
roli_mod = 1370757747362922367
roli_r = 1
roli_table = [0]
roli_rr = 1
for i in range(3 * (n - 1)):
    roli_table.append((roli_table[-1] + roli_rr * s[i]) % roli_mod)
    roli_rr *= roli_r
    roli_rr %= roli_mod


def roli_hash(i, j):
    return (roli_table[j + 1] - roli_table[i] + roli_mod) % roli_mod * pow(roli_r, roli_mod - 1 - i, roli_mod) % roli_mod


def roli_check(i1, j1, i2, j2):
    return roli_hash(i1, j1) == roli_hash(i2, j2)


ans = []
for k in range(n - 1, 2 * (n - 1) + 1):
    if roli_check(0, n - 2, k, k + (n - 1) - 1):
        ans.append(k - (n - 1))
for i in ans:
    print(i, a[i] ^ b[0])
