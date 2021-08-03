import sys
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

st = set()
idx = 0

i = 0
j = 0
while i < n and a[i] == 0:
    i += 1
while j < n and a[i] != b[j]:
    j += 1

b = b[j:] + b[:j]
j = 0
while i < n:
    if a[i] != 0:
        while j < n and b[j] == 0:
            j += 1
        if b[j] != a[i] or j == n:
            print('NO')
            return
        j += 1
    i += 1
print('YES')
