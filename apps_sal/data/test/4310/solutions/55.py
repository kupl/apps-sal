import math
a = list(map(int, input().split()))
q = []
for i in range(3):
    for j in range(3):
        if not i == j:
            q.append(abs(a[i] - a[j]) + abs(a[j] - a[3 - (i + j)]))
print(min(q))
