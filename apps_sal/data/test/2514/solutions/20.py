from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
d = defaultdict(int)
ans = 0
for a in A:
    ans += a
    d[a] += 1
for _ in range(Q):
    (b, c) = map(int, input().split())
    n = d[b]
    ans -= n * b
    ans += n * c
    print(ans)
    d[b] = 0
    d[c] += n
