from collections import deque

n, d, a = map(int, input().split())
xh = sorted([list(map(int, input().split())) for _ in range(n)])

ans = 0
dam_sum = 0
q = deque()
for i, (x, h) in enumerate(xh):
    while q and q[0][0] < x:
        ran, dam = q.popleft()
        dam_sum -= dam
    h -= dam_sum
    if h <= 0:
        continue 
    c = -(-h//a)
    ans += c
    dam_sum += c*a
    q.append((x+d*2, c*a))
print(ans)
