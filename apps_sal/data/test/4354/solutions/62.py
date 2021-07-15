import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ab = []
cd = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))
for _ in range(m):
    c, d = map(int, input().split())
    cd.append((c, d))
ans = []
for a, b in ab:
    t = 10**18
    checkpoint = -1
    for i, cdi in enumerate(cd):
        c, d = cdi
        dist = abs(a-c)+abs(b-d)
        if dist < t:
            t = dist
            checkpoint = (i+1)
    ans.append(checkpoint)
print(*ans, sep='\n')

