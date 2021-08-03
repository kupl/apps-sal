from collections import Counter
S = input()
SC = Counter(S)
a = SC['a']
print(min(len(S), 2 * a - 1))
