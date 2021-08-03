from collections import Counter
input()
a = list(map(int, input().split()))

c = Counter(a).most_common(1)
print(c[0][1])
