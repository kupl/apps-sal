import collections
n = int(input())
alist = [int(input()) for i in range(n)]
cole = collections.Counter(alist)
count = 0
for i in cole.values():
    if i % 2 == 1:
        count += 1
print(count)
