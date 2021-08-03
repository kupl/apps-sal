from collections import Counter
n = int(input())
a = [int(x) for x in input().split() if x != '0']
print(len(Counter(a)))
