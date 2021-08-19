import math
import sys
input = sys.stdin.readline
(n, I) = list(map(int, input().split()))
A = list(map(int, input().split()))
k = math.floor(I * 8 / n)
K = 2 ** min(k, 20)
s = sorted(set(A))
dis = len(s)
count = {}
for i in range(n):
    if A[i] not in count:
        count[A[i]] = 1
    else:
        count[A[i]] += 1
diff = max(dis - K, 0)
ct = 0
for i in range(diff):
    ct += count[s[i]]
ans = ct
for i in range(diff - 1, -1, -1):
    ct -= count[s[i]]
    ct += count[s[i + K]]
    ans = min(ans, ct)
print(ans)
