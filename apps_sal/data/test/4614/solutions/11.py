from collections import Counter
l = list(map(int, input().split()))
l = list(Counter(l).most_common())
print(l[1][0])
