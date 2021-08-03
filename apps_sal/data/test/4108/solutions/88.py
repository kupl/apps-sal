#!/usr/bin/env python3
from collections import Counter
def x(): return sorted(Counter(input()).values())


print(('YNeos'[x() != x()::2]))
