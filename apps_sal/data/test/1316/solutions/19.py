import sys
import math


def read_int():
    return int(input().strip())


def read_int_list():
    return list(map(int, input().strip().split()))


def read_string():
    return input().strip()


def read_string_list(delim=" "):
    return input().strip().split(delim)


n, k = read_int_list()

s = read_string()

seen_distincts = {}
start = 0
while start < n - k + 1:
    temp_dist = s[start]
    broken = 0
    broken_at = -1

    for i in range(1, k):
        if s[start + i] == temp_dist:
            pass
        else:
            broken = 1
            broken_at = start + i
            break

    if broken:
        start = broken_at
    else:
        seen_distincts[temp_dist] = seen_distincts.get(temp_dist, 0) + 1
        start += k

maxi = 0
for k in seen_distincts:
    maxi = max(maxi, seen_distincts[k])

print(maxi)
