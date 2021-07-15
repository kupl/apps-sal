from collections import Counter

c = Counter(input())
print(min(c['B'], c['u'] // 2, c['l'], c['b'], c['a'] // 2, c['s'], c['r']))
