# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, k, Q = map(int, readline().split())
*a, = map(int, readline().split())
*sa, = sorted(a)
a.append(-1)
ans = 10**9
for i in sa:
    q = []
    v = []
    for j in a:
        if j < i:
            if len(v) >= k:
                v.sort()
                q += v[:len(v) - k + 1]
            v.clear()
        else:
            v.append(j)

    if len(q) < Q: break
    q.sort()
    ans = min(ans, q[Q - 1] - q[0])

print(ans)
