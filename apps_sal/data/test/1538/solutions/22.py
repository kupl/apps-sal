from collections import Counter
n = int(input())
a = Counter(list(map(int, input().split())))
print(a.most_common()[0][1])
