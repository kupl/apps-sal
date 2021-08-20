from collections import Counter
n = int(input())
a = list(input())
c = Counter(a)
print(min(n // 11, c['8']))
