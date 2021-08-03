from collections import Counter
n = int(input())
a = [int(i) for i in input().split()]
cnt = Counter(a)
l = len(cnt)
even = 0
for v in cnt.values():
    if v % 2 == 0:
        even += 1
print(l if even % 2 == 0 else l - 1)
