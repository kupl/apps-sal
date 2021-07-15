from collections import Counter

n, k = list(map(int, input().split()))
a = tuple(Counter(input().split()).values())
print(len(a) * ((max(a) - 1) // k + 1) * k - sum(a))

