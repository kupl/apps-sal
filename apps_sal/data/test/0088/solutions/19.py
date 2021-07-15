#!/usr/bin/env python3
a, b = list(map(int,input().split()))
cnt = 0
for i in range(2,64*8):
    for j in range(1,i):
        c = ['1'] * i
        c[j] = '0'
        c = int(''.join(c), 2)
        if a <= c <= b:
            cnt += 1
print(cnt)

