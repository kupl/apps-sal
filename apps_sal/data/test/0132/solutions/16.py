n = int(input())
angles = list(map(int, input().split()))
angles = angles + angles
sum_ = 0
from_ = 0
best = 360
for to in range(n):
    sum_ += angles[to]
    while sum_ >= 180:
        best = min(best, abs(360 - 2 * sum_))
        sum_ -= angles[from_]
        from_ += 1
    best = min(best, abs(360 - 2 * sum_))
print(best)
