from collections import deque
n = int(input())
cnt = 0
d = {n: 0}
q = deque([n])
while q[0] > -5:
    t = q.popleft()
    cnt = d[t]
    # print(t)
    a = 1
    b = 1
    while 6**a <= t:
        a += 1
    while 9**b <= t:
        b += 1
    a -= 1
    b -= 1
    # print(t,a,b)
    if t - 6**a in d:
        if d[t - 6**a] > cnt + 1:
            d[t - 6**a] = cnt + 1
            q.append(t - 6**a)
    else:
        d[t - 6**a] = cnt + 1
        q.append(t - 6**a)
    if t - 9**b in d:
        if d[t - 9**b] > cnt + 1:
            d[t - 9**b] = cnt + 1
            q.append(t - 9**b)
    else:
        d[t - 9**b] = cnt + 1
        q.append(t - 9**b)
    # print(q)
print((d[0]))
# print(d)
