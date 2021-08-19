#! /usr/bin/env python

n, m = [int(x) for x in input().split()]
dancers = {}
for i in range(m):
    dance = [int(x) for x in input().split()]
    for j in range(3):
        if dance[j] not in dancers:
            dancers[dance[j]] = j
        else:
            dancers[dance[(j + 1) % 3]] = (dancers[dance[j]] + 1) % 3
            dancers[dance[(j + 2) % 3]] = (dancers[dance[j]] + 2) % 3
            break

print(*[x + 1 for x in list(dancers.values())])
