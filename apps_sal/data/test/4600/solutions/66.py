(n, m) = list(map(int, input().split()))
wa = [0] * (n + 1)
ac = [0] * (n + 1)
for _ in range(m):
    (p, s) = input().split()
    p = int(p)
    if s == 'WA' and ac[p] == 0:
        wa[p] += 1
    elif s == 'AC':
        ac[p] = 1
for (i, ok) in enumerate(ac):
    if not ok:
        wa[i] = 0
print('{} {}'.format(sum(ac), sum(wa)))
