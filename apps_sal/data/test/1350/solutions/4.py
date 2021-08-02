import sys
import string


def ria():
    return [int(i) for i in input().split()]


n, k = ria()
mp = {}
for i in string.ascii_uppercase[:k]:
    mp[i] = 0
for i in input():
    if i in mp:
        mp[i] += 1
print(min(mp.values()) * k)
