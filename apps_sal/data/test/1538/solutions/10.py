from collections import Counter

n = int(input())
a = list(map(int, input().split()))

print(max(list(Counter(a).values())))

