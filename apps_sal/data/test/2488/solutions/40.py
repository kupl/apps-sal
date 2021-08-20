from collections import deque
(N, D, A) = map(int, input().split())
X = [0] * N
for i in range(N):
    (x, h) = map(int, input().split())
    X[i] = (x, h)
X = sorted(X)
q = deque()
ans = 0
total = 0
for i in range(N):
    (x, h) = X[i]
    while len(q) > 0 and q[0][0] < x:
        total -= q[0][1]
        q.popleft()
    h -= total
    if h > 0:
        num = (h + A - 1) // A
        ans += num
        damage = num * A
        total += damage
        q.append((x + 2 * D, damage))
print(ans)
