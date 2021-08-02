from collections import deque
n, x = map(int, input().split())
d = list(map(int, input().split()))

q = deque([])
sum_q = 0

sq = deque([])
sum_sq = 0

for i in range(n):

    q.append(d[i])
    sum_q += d[i]

    sq.append((d[i] + 1) * d[i] // 2)
    sum_sq += (d[i] + 1) * d[i] // 2

ans = 0

for i in range(n):

    q.append(d[i])
    sum_q += d[i]
    sq.append((d[i] + 1) * d[i] // 2)
    sum_sq += (d[i] + 1) * d[i] // 2

    while sum_q - q[0] >= x:
        sum_q -= q.popleft()
        sum_sq -= sq.popleft()
    #print (q,sq,sum_q,sum_sq)

    origin = sum_sq - sq[0]
    remday = x - (sum_q - q[0])
    differ = (q[0] + q[0] - remday + 1) * remday // 2
    #print (origin,remday,differ)

    ans = max(ans, origin + differ)

print(ans)
