from collections import Counter
from itertools import combinations
(n, m) = map(int, input().split())
genres = Counter(map(int, input().split()))
count = 0
for (a, b) in combinations(range(1, m + 1), 2):
    count += genres[a] * genres[b]
print(count)
