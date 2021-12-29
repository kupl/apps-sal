from itertools import product
(n, m, x) = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(n)]
cost = -1
for cand in product((0, 1), repeat=n):
    tmp = 0
    scores = [0] * m
    for (bought, ca) in zip(cand, CA):
        if not bought:
            continue
        for i in range(1, m + 1):
            scores[i - 1] += ca[i]
        tmp += ca[0]
    if min(scores) >= x and (cost == -1 or tmp < cost):
        cost = tmp
print(cost)
