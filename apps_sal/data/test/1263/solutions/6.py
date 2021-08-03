n, k = [int(x) for x in input().split(' ')]

taste = [int(x) for x in input().split(' ')]
cal = [int(x) for x in input().split(' ')]

w = [taste[i] - k * cal[i] for i in range(n)]

taste_per_diff = [-1 for i in range(50000)]
shift = 20000

taste_per_diff[shift] = 0

for i in range(n):
    new_tpd = [x for x in taste_per_diff]
    for j in range(0, 40000):
        if taste_per_diff[j] != -1:
            new_tpd[j + w[i]] = max(new_tpd[j + w[i]], taste_per_diff[j] + taste[i])

    taste_per_diff = new_tpd

if taste_per_diff[shift] == 0:
    print(-1)
else:
    print(taste_per_diff[shift])
