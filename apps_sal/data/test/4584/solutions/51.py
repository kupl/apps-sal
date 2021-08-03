from collections import Counter

n = int(input())
a = list(map(int, input().split()))

s = Counter(a)

for i in range(1, n + 1):
    print(s[i])
