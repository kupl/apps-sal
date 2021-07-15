input()
a = list(map(int, input().split()))

from collections import Counter
c = Counter(a).most_common(1)
print(c[0][1])

