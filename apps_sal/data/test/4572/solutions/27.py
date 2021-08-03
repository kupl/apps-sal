import sys
import collections
s = list(input())
a = collections.Counter(s)

for i in range(97, 97 + 26):
    if chr(i) not in a:
        print(chr(i))
        return
else:
    print("None")
