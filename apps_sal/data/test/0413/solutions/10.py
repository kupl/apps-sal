3
# -*- coding: utf-8 -*-

n, m = list(map(int, input().split()))
mem = [2**30] * 4 * (max(n, m))
mem[n] = 0
q = [n]
while q:
    c = q.pop(0)
    if 2 * c < len(mem) and mem[2 * c] > mem[c] + 1:
        q.append(2 * c)
        mem[2 * c] = mem[c] + 1
    if c > 1 and mem[c - 1] > mem[c] + 1:
        q.append(c - 1)
        mem[c - 1] = mem[c] + 1
print(mem[m])

