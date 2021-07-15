import sys

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

n = read_int()
a = read_ints()

for i in range(n):
    if a[a[a[i] - 1] - 1] == i + 1:
        print('YES')
        return

print('NO')

