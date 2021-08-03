# D - Candy Distribution
# https://atcoder.jp/contests/abc105/tasks/abc105_d

from collections import Counter

n, m = list(map(int, input().split()))
A = list(map(int, input().split()))

accr = [0] * (n + 1)

for i in range(n):
    accr[i + 1] = accr[i] + A[i]

li = [i % m for i in accr]

C = Counter(li)

ans = 0
for v in list(C.values()):
    if v > 1:
        ans += v * (v - 1) // 2

print(ans)
