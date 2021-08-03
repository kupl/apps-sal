from bisect import bisect_left
from string import ascii_lowercase

s = input()
t = input()
n = len(s)

dict_s = {c: [] for c in ascii_lowercase}
for i, c in enumerate(s * 2):
    dict_s[c].append(i)

for c in ascii_lowercase:
    if not dict_s[c]:
        del dict_s[c]


dict_next_i = {
    c: [dict_s[c][bisect_left(dict_s[c], i + 1)] for i in range(n)]
    for c in list(dict_s.keys())
}


def next_i(i, c):
    return n * (i // n) + dict_next_i[c][i % n]


def answer():
    if not all(c in s for c in t):
        return -1
    i = -1
    for c in t:
        i = next_i(i, c)
    return i + 1  # 1-origin


print((answer()))
