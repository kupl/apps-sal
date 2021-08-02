import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy


X, Y = map(int, input().split())

print("Brown" if abs(X - Y) <= 1 else "Alice")
