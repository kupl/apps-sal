from collections import Counter
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a = dict(Counter(a))
count = 0
for i in a.values():
    if i % 2 == 1:
        count += 1
print(count)
