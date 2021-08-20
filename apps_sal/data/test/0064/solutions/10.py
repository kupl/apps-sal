from collections import Counter
(n, k) = [int(v) for v in input().split()]
s = input().strip()
cnt = Counter(s)
print(['NO', 'YES'][all([v <= k for v in cnt.values()])])
