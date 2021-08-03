from collections import Counter
s = int(input())
a = list(map(int, input().split()))
b = Counter(a)
total = 0
for i in b.values():
    total += i * (i - 1) // 2
for i in a:
    print(total - b[i] * (b[i] - 1) // 2 + (b[i] - 1) * (b[i] - 2) // 2)
