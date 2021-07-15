from collections import Counter

ABC = list(map(int, input().split()))

cnt = Counter(ABC)
values, counts = zip(*cnt.most_common(2))

print(values[1])
