# -*- coding: utf-8 -*-

k = int(input())

counter = [0] * 10
s = ''.join([input().strip() for i in range(4)])

for c in s:
    if c == '.':
        continue
    counter[int(c)] += 1

m = max(counter)
print('NO' if m > 2 * k else 'YES')
