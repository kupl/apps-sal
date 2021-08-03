from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    diff = [y - x for x, y in zip(a, b)]

    if min(diff) < 0:
        print('NO')
        continue

    group = [len(tuple(v)) for k, v in groupby(diff) if k > 0]
    if len(group) > 1:
        print('NO')
    else:
        print('YES')
