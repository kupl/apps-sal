(n, m) = map(int, input().split())
A = list(map(int, input().split()))
votes = sum(A)
tot = 0
for i in range(n):
    std = votes * (1 / (4 * m))
    if A[i] < std:
        continue
    tot += 1
if tot >= m:
    print('Yes')
else:
    print('No')
