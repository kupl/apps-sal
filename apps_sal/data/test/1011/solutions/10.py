__author__ = 'zhan'

first = []
second = []

n = int(input())
line = input().split()
for i in range(n):
    first.append(int(line[i]))
first.sort()

m = int(input())
line = input().split()
for i in range(m):
    second.append(int(line[i]))
second.sort()


a = 3 * n
b = 3 * m
d = a - b
penalty = [0, 0]
i = 0
j = 0

while i < n and j < m:
    t = min(first[i], second[j])
    while i < n and first[i] <= t:
        i += 1
        penalty[0] += 1
    while j < m and second[j] <= t:
        j += 1
        penalty[1] += 1
    if 3*n - penalty[0] - 3*m + penalty[1] > d:
        a = 3 * n - penalty[0]
        b = 3 * m - penalty[1]
        d = 3*n - penalty[0] - 3*m + penalty[1]

if 2 * n - 2 * m > d:
    a = 2 * n
    b = 2 * m

print(str(a)+":"+str(b))


