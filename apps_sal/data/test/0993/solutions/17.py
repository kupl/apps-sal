from itertools import accumulate
n, m = list(map(int, input().split()))
A = tuple(map(int, input().split()))

AS = [0] + list(accumulate(A))
counts = dict()
for a in AS:
    r = a % m
    counts.setdefault(r, 0)
    counts[r] += 1

ans = 0
for k, v in list(counts.items()):
    ans += v * (v - 1) // 2
print(ans)
