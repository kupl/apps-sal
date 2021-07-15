__author__ = 'zhan'

n = int(input())
first = sorted([int(i) for i in input().split()])

m = int(input())
second = sorted([int(i) for i in input().split()])

a = pa = 3 * n
b = pb = 3 * m
d = a - b

i = 0
j = 0

while i < n and j < m:
    t = min(first[i], second[j])
    while i < n and first[i] <= t:
        i += 1
        pa -= 1
    while j < m and second[j] <= t:
        j += 1
        pb -= 1
    if pa - pb > d:
        a = pa
        b = pb
        d = pa - pb

if 2 * n - 2 * m > d:
    a = 2 * n
    b = 2 * m

print(str(a)+":"+str(b))


