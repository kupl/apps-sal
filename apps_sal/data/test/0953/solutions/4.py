#!/usr/bin/env python3

n = int(input())
p = [int(x) for x in input().split()]
a = [[int(c) for c in input()] for _ in range(n)]

exchange = []
for i in range(n):
    s = set()
    s.add(i)
    for j in range(n):
        if a[i][j] == 1:
            s.add(j)
    if len(s) > 1:
        exchange.append(s)


i = 0
while i < len(exchange) - 1:
    j = i + 1
    while j < len(exchange):
        if exchange[i] & exchange[j]:
            exchange[i] |= exchange[j]
            exchange.pop(j)
            j = i + 1
        else:
            j += 1
    i += 1
exchange = [sorted(s) for s in exchange]


for ex in exchange:
    for i in range(len(ex) - 1):
        for j in range(i + 1, len(ex)):
            if p[ex[i]] > p[ex[j]]:
                p[ex[i]], p[ex[j]] = p[ex[j]], p[ex[i]]


print(" ".join(map(str, p)))
