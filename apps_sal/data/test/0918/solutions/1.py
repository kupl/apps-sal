#!/usr/bin/env python3

try:
    while True:
        n, m = list(map(int, input().split()))
        d = [[] for i in range(m)]
        for i in range(n):
            name, region, score = input().split()
            region = int(region) - 1
            score = int(score)
            d[region].append((score, name))
        for i in range(m):
            ls = d[i]
            ls.sort(reverse=True)
            if len(ls) > 2 and ls[1][0] == ls[2][0]:
                print('?')
            else:
                print(ls[0][1], ls[1][1])

except EOFError:
    pass
