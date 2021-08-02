#! /bin/python
n = int(input())
tab = str(input())

d = 1
tmp = 1
changes = 1
for i in range(1, n):
    if tab[i] != tab[i - 1]:
        changes += 1
print(min(changes + 2, n))
