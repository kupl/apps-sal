from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A).most_common()
even = 0
for (k, v) in cnt:
    if v % 2 == 0:
        even += 1
print(len(set(A)) - even % 2)
