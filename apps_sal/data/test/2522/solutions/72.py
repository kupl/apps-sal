from collections import defaultdict
from collections import Counter as co
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
D, E = co(A), co(B)
for i in D:
    if D[i] + E[i] > N:
        print('No')
        return

d = defaultdict(int)
for i, e in enumerate(A):
    d[e] = i
ans = 0
for i, e in enumerate(B):
    ans = max(ans, (d[e] - i + 1))
s = B[-ans:] + B[:-ans]
print('Yes')
print(*s)
