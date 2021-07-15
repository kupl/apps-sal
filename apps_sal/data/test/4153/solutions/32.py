# author:  Taichicchi
# created: 12.09.2020 12:29:36

from collections import Counter
import sys

S = input()

c = Counter(S)

print((len(S) - abs(c["0"] - c["1"])))

