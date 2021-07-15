from collections import defaultdict
N, M = map(int,input().rstrip().split())
d = defaultdict(lambda: 0)
for _ in range(N):
    A, B = map(int,input().rstrip().split())
    d[A] += B
ans=0
for k in sorted(d.keys()):
    if d[k]<=M:
        ans += k*d[k]
    else:
        ans += k*M
    M -= d[k]
    if M<=0:break
print(ans)
