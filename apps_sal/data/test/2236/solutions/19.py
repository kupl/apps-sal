from collections import Counter
from itertools import accumulate
n = int(input())
print(n - Counter(accumulate(list(map(int, input().split())), lambda x, y: x+y)).most_common(1)[0][1])

