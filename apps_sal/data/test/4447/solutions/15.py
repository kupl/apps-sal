(n, m) = list(map(int, input().split()))
aa = list(map(int, input().split()))
(res, cnt) = (sum(aa), [-n // m] * m)
acc = [[] for _ in range(m)]
for (i, a) in enumerate(aa):
    r = a % m
    cnt[r] += 1
    acc[r].append(i)
(icnt, a) = ([], 0)
for c in cnt:
    a += c
    icnt.append(a)
start = (min(range(m), key=icnt.__getitem__) + 1) % m
(excess, scarce) = ([], [])
for r in (range(start, m), range(start)):
    for i in r:
        if cnt[i] > 0:
            for _ in range(cnt[i]):
                excess.append(i)
        elif cnt[i] < 0:
            for _ in range(-cnt[i]):
                scarce.append(i)
for (e, s) in zip(excess, scarce):
    aa[acc[e].pop()] += (s - e) % m
print(sum(aa) - res)
print(' '.join(map(str, aa)))
