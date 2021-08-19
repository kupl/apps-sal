from collections import Counter
N = int(input())
A = list(map(int, input().split()))
c = Counter(A)
eat = 0
for v in c.most_common():
    if v[1] >= 2:
        eat += v[1] - 1
if eat % 2 != 0:
    eat += 1
print(N - eat)
