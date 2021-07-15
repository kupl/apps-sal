nm = list(map(int, input().split()))
n, m = nm[0], nm[1]
ab_list = [list(map(int, input().split())) for _ in range(m)]
results = dict([(i, 0) for i in range(1, n + 1)])
for ab in ab_list:
    results[ab[0]] += 1
    results[ab[1]] += 1

for i in range(1, n + 1):
    print((results[i]))

