s = list(input())
import collections
import sys
a = collections.Counter(s)

for i in range(97,97+26):
    if chr(i) not in a:
        print(chr(i))
        return
else:
    print("None")
