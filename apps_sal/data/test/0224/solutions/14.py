import math
import sys
import re
import itertools
import pprint
import collections
(ri, rai) = (lambda: int(input()), lambda: list(map(int, input().split())))
s = input()
t = list([len(x) for x in re.split('[AEIOUY]+', s)])
print(max(t) + 1)
