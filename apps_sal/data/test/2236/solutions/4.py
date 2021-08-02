from collections import *
from itertools import *
print(int(input()) - max(Counter(accumulate(list(map(int, input().split())))).values()))
