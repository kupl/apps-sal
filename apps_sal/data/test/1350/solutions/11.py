from collections import Counter
(n, k) = list(map(int, input().split()))
s = input()
letters = list(s)
c = dict(Counter(letters))
if len(c) < k:
    print(0)
else:
    print(k * min(c.values()))
