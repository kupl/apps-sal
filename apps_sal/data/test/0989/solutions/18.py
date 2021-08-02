# encoding: utf-8
from sys import stdin

n, k = [int(i) for i in stdin.readline().strip().split()]
a = [int(i) for i in stdin.readline().strip().split()]
a.sort()

i = 0
j = n - 1
a_min = a[i]
a_max = a[j]
while i < j:
    if i + 1 <= n - j:
        required_steps = (a[i + 1] - a[i]) * (i + 1)
        if required_steps > k:
            a_min += k // (i + 1)
            break
        else:
            i += 1
            k -= required_steps
            a_min = a[i]
    else:
        required_steps = (a[j] - a[j - 1]) * (n - j)
        if required_steps > k:
            a_max -= k // (n - j)
            break
        else:
            j -= 1
            k -= required_steps
            a_max = a[j]

print(a_max - a_min)
