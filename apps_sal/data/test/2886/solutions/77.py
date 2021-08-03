import sys
import string

alphabets = list(string.ascii_lowercase)

s = input()

l = len(s)


def hm(a, string): return sum([x == a for x in string])


for x in range(l - 1):
    if s[x] == s[x + 1]:
        print('{} {}'.format(x + 1, x + 2))
        return


for n in range(l - 3):
    for a in alphabets:
        if hm(a, s[n:n + 3]) > 1:
            print('{} {}'.format(n + 1, n + 3))
            return
print('-1 -1')
