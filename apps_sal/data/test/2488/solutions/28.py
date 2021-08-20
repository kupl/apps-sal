from collections import deque
(n, d, a) = list(map(int, input().split()))
mons = []
for i in range(n):
    (x, h) = list(map(int, input().split()))
    mons.append((x, h))
mons = sorted(mons)
q = deque()
dm_sum = 0
ans = 0
for i in range(n):
    while dm_sum > 0:
        if q[0][0] < mons[i][0]:
            cur = q.popleft()
            dm_sum -= cur[1]
        else:
            break
    if mons[i][1] <= dm_sum:
        continue
    rem = mons[i][1] - dm_sum
    at_num = rem // a
    if rem % a != 0:
        at_num += 1
    ans += at_num
    q.append((mons[i][0] + 2 * d, at_num * a))
    dm_sum += at_num * a
print(ans)
