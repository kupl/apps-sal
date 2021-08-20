import itertools
(n, l, r, x) = [int(c) for c in input().split()]
c = [int(c) for c in input().split()]
c.sort()
count = 0
for i in range(2, n + 1):
    combs = itertools.combinations(c, i)
    for comb in combs:
        min = comb[0]
        max = comb[0]
        sum = 0
        for a in comb:
            sum += a
            if a > max:
                max = a
            if a < min:
                min = a
        if sum >= l and sum <= r and (max - min >= x):
            count += 1
print(count)
