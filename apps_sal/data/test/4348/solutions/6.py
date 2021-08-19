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


# code goes here
n, k = viread()
s = read()
letters = Counter(s)
# print(letters)
for l in sorted(letters.keys()):
    # print(letters[l], l + "'s")
    if letters[l] < k:
        s = re.sub(l, "", s)
        k -= letters[l]
        # print(s)
    else:
        news = ""
        hits = 0
        for c in s:
            # print("looking at", c)
            # print("hits is", hits)
            if c == l:
                hits += 1
                # print("hit!")
            if c != l or hits > k:
                news += c
                # print(news)
        s = news
        break

print(s)
