from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
s = 0
ans = n - 1
for i in range(n):
    t = A[i]
    s += t
    d[s] += 1
    ans = min(ans, n - d[s])
print(ans)
