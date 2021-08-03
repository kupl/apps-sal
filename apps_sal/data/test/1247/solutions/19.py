from collections import Counter
cnt = Counter(input())
s = sum([a[1] % 2 for a in list(cnt.items())])
print('First' if s <= 1 or s % 2 else 'Second')
