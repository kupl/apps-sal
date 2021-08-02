from collections import Counter
n = int(input())
a = list(map(int, input().split()))
l = Counter(a)
for i in range(n):
    print(l[i + 1])
