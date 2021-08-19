#!/usr/env python3

n, m, k = map(int, input().split())
a = [int(x) for x in input().split()]  # a[p] = id of app at position p (p=0,1,2,...)
b = [int(x) for x in input().split()]
assert(len(a) == n)
assert(len(b) == m)
pos = [0] * (n + 1)  # c[i] = position of app with id i (id=1,2,3,...)
for p in range(n):
    pos[a[p]] = p
gesture = 0
for i in b:
    this_pos = pos[i]
    this_id = i

    gesture += this_pos // k + 1

    if this_pos > 0:
        prev_pos = pos[i] - 1
        prev_id = a[prev_pos]

        a[this_pos], a[prev_pos] = a[prev_pos], a[this_pos]
        pos[this_id], pos[prev_id] = pos[prev_id], pos[this_id]
print(gesture)
