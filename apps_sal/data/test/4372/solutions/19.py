import sys


def hcf(a, b):
    while a:
        temp = a
        a = b % a
        b = temp
    return b


n = int(sys.stdin.readline())

a = [int(i) for i in sys.stdin.readline().split()]

val = max(a)

m = val - a[0]

tmp_sum = 0

for x in range(n):
    m = hcf(val - a[x], m)
    tmp_sum += val - a[x]

print(tmp_sum // m, m)
