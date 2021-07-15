from collections import Counter
input()
a = map(int, input().split())
b = Counter(a)
b = list(b.values())
print(sum(b) - max(b))
