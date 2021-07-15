n = int(input())
m = int(input())

aa = []
for i in range(n):
    aa += [int(input())]

maxAns = max(aa) + m

rest = max(aa) * n - sum(aa)
if m <= rest:
    minAns = max(aa)
else:
    m -= rest
    minAns = max(aa) + (m + n - 1) // n

print(minAns, maxAns)
