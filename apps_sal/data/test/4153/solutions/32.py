from collections import Counter
import sys
S = input()
c = Counter(S)
print(len(S) - abs(c['0'] - c['1']))
