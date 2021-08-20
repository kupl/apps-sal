from collections import deque
(N, K) = map(int, input().split())
table = list(map(int, input().split()))
jnum = K - sum((1 for i in table if i >= 0))
num_mins = sum((1 for i in table if i < 0))
q_plus = deque(sorted([i for i in table if i >= 0], reverse=True))
q_mins = deque(sorted([-i for i in table if i < 0], reverse=True))
s_plus = []
s_mins = []
total = 1
if K % 2 == 1 and N == num_mins or (N == K and num_mins % 2 == 1):
    for i in range(K):
        if not q_plus:
            total = -total * q_mins.pop() % (10 ** 9 + 7)
        elif not q_mins:
            total = total * q_plus.pop() % (10 ** 9 + 7)
        elif q_plus[-1] > q_mins[-1]:
            total = -total * q_mins.pop() % (10 ** 9 + 7)
        else:
            total = total * q_plus.pop() % (10 ** 9 + 7)
    total = total % (10 ** 9 + 7)
else:
    for i in range(K):
        if not q_plus:
            s_mins.append(q_mins.popleft())
        elif not q_mins:
            s_plus.append(q_plus.popleft())
        elif q_plus[0] > q_mins[0]:
            s_plus.append(q_plus.popleft())
        else:
            s_mins.append(q_mins.popleft())
    if len(s_mins) % 2 == 1:
        if not q_plus:
            s_plus[-1] = q_mins[0]
        elif not q_mins or not s_plus:
            s_mins[-1] = q_plus[0]
        elif q_mins[0] * s_mins[-1] > q_plus[0] * s_plus[-1]:
            s_plus[-1] = q_mins[0]
        else:
            s_mins[-1] = q_plus[0]
    s_plus.extend(s_mins)
    for j in s_plus:
        total = total * j % (10 ** 9 + 7)
print(total)
