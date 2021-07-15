import sys

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

n, k = read_ints()
a = read_ints()

res_i, res_q = 0, 0
for i, b in enumerate(a):
    if n - n % b > a[res_i] * res_q:
        res_i, res_q = i, n // b

print(res_i + 1, res_q)

