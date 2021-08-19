from collections import deque
(X, Y, A, B, C) = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
ALL = p + q + r
ALL.sort(reverse=True)
ALL = deque(ALL)
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
p = deque(p)
q = deque(q)
r = deque(r)
ans = 0
p_cnt = 0
q_cnt = 0
r_cnt = 0
loopcnt = 0
while loopcnt < X + Y:
    apple = ALL.popleft()
    if p_cnt < X and apple == p[0]:
        ans += p.popleft()
        p_cnt += 1
        loopcnt += 1
    elif q_cnt < Y and apple == q[0]:
        ans += q.popleft()
        q_cnt += 1
        loopcnt += 1
    elif r_cnt < C and apple == r[0]:
        ans += r.popleft()
        r_cnt += 1
        loopcnt += 1
print(ans)
