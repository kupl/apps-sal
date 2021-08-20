M = 10 ** 5
n = int(input())
ss = [int(s) for s in input().split()]
prime_factor = [set() for i in range(M + 1)]
for p in range(2, M + 1):
    if prime_factor[p] != set():
        continue
    else:
        for i in range(p, M + 1, p):
            prime_factor[i].add(p)
cnt = [0] * (M + 1)
for s in ss:
    for p in prime_factor[s]:
        cnt[p] += 1
print(max(1, max(cnt)))
