MOD = (10**9) + 7

n, l, r = list(map(int, input().split()))


def find_ks(l, r):
    num_elems = (r - l + 1)
    num_trips = int(num_elems / 3)
    k = [num_trips] * 3

    start_idx = l % 3
    count = num_elems % 3

    for i in range(count):
        k[(start_idx + i) % 3] += 1

    return k


k = find_ks(l, r)
f = [[0 for _ in range(3)] for _ in range(n)]


for mod in range(3):
    f[0][mod] = k[mod]

for idx in range(1, n, 1):
    for mod in range(3):
        f[idx][mod] += (f[idx - 1][mod] * k[0]) % MOD
        f[idx][mod] = f[idx][mod] % MOD

        f[idx][mod] += (f[idx - 1][(mod - 1) % 3] * k[1]) % MOD
        f[idx][mod] = f[idx][mod] % MOD

        f[idx][mod] += (f[idx - 1][(mod - 2) % 3] * k[2]) % MOD
        f[idx][mod] = f[idx][mod] % MOD


print(f[n - 1][0] % MOD)
