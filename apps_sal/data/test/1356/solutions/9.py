from collections import Counter
s = input()
c = Counter(list(s))
print(min(len(s), 2 * c['a'] - 1))
