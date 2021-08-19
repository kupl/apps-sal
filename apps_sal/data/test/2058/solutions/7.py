#!/usr/bin/env python3

a, b = input(), input()
alen, blen = len(a), len(b)  # blen >= alen

diff = blen - alen
count = b[:diff + 1].count('0')
result = 0
for i in range(0, alen):
    #print('at i=%d, count=%d' % (i, count))
    result += diff + 1 - count if a[i] == '0' else count
    #print('compared at', i, diff+i+1)
    if i == alen - 1:
        break
    count -= 1 if b[i] == '0' else 0
    count += 1 if b[diff + 1 + i] == '0' else 0
print(result)
