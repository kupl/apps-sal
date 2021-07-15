from collections import Counter

input()
a = Counter(map(int, input().split()))
print(sum(v - k if k <= v else v for k, v in a.items()))
