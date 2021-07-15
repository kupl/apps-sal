#!/usr/bin/env python3
from sys import stdin, stdout, exit

stdin.readline()
x, k, y = [int(i) for i in stdin.readline().split(' ') if i]
a = [int(i) for i in stdin.readline().split(' ') if i]
b = [int(i) for i in stdin.readline().split(' ') if i]

a[:0] = [0]
a.append(0)
b.append(0)

if x >= y * k:  # BS cheaper or same
    def calc(a):
        n = len(a) - 2
        if max(a) == max(a[0], a[-1]):
            return n * y
        if n < k:
            stdout.write('-1\n')
            return
        return (n - k) * y + x
else:  # FB cheaper
    def calc(a):
        n = len(a) - 2
        if n < k:
            if max(a) == max(a[0], a[-1]):
                return n * y
            stdout.write('-1\n')
            return
        return n // k * x + n % k * y

n = 0
i = 0
for j in b:
    t = i + 1
    while t < len(a):
        if a[t] == j:
            break
        t += 1
    else:
        stdout.write('-1\n')
        return
    if t > i + 1:
        n += calc(a[i: t + 1])
    i = t
stdout.write(f'{n}\n')

