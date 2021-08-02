import sys


def fact(k):
    return k ** 2 * (k - 1) ** 2 * (k - 2) ** 2 * (k - 3) ** 2 * (k - 4) ** 2


s = input()

s1 = s[0] + s[2] + s[4] + s[3] + s[1]

n = int(s1)

k = n ** 5

s = str(k % 100000)

while len(s) < 5:
    s = '0' + s

print(s)
