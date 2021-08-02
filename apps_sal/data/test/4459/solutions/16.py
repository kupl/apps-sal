from collections import Counter
input()
a = Counter(map(int, input().split()))
print(sum(j if i > j else j - i for i, j in a.items()))
