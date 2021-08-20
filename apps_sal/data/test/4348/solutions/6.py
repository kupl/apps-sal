from collections import Counter
import re
import math
import decimal
import bisect


def read():
    return input().strip()


def iread():
    return int(input().strip())


def viread():
    return list(map(int, input().strip().split()))


(n, k) = viread()
s = read()
letters = Counter(s)
for l in sorted(letters.keys()):
    if letters[l] < k:
        s = re.sub(l, '', s)
        k -= letters[l]
    else:
        news = ''
        hits = 0
        for c in s:
            if c == l:
                hits += 1
            if c != l or hits > k:
                news += c
        s = news
        break
print(s)
