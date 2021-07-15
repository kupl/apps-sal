from collections import Counter

n = int(input())
a = list(map(int, input().split()))

count = 0

for i, j in Counter(a).items():
    if j-i < 0:
        count += j
    else:
        count += min(j-i, j)

print(count)
