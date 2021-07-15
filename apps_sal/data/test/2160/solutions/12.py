import sys
input = sys.stdin.readline
from collections import defaultdict

def lose(i, j):
    if i==j:
        return i in s
    else:
        return (i in s) and (j in s) and (first[i]<last[j])

n, k = map(int, input().split())
x = list(map(int, input().split()))
x = list(map(lambda x: x-1, x))
s = set(x)
first = defaultdict(int)
last = defaultdict(int)

for i in range(k):
    if x[i] not in first:
        first[x[i]] = i
    
for i in range(k-1, -1, -1):
    if x[i] not in last:
        last[x[i]] = i

ans = 3*n-2

for i in range(n):
    for j in range(max(i-1, 0), min(i+2, n)):
        if lose(i, j):
            ans -= 1

print(ans)
