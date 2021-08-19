n_max = 10 ** 5 + 10
sieve = [0, 0] + [1] * n_max
m = 2
while m * m <= n_max:
    if sieve[m]:
        for n in range(2 * m, n_max, m):
            sieve[n] = 0
    m += 1
ok = [0] * n_max
cums = [0]
for n in range(n_max):
    if sieve[n] and sieve[(n + 1) // 2]:
        ok[n] = 1
    cums.append(cums[-1] + ok[n])
q = int(input())
for i in range(q):
    (l, r) = map(int, input().split())
    print(cums[r + 1] - cums[l])
