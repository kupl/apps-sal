from collections import deque
(n, k) = list(map(int, input().split()))
v = list(map(int, input().split()))
d = deque(v)
t = min(n, k)
score = 0
for a in range(t + 1):
    for b in range(t - a + 1):
        tmp_d = d.copy()
        jems = []
        for i in range(a):
            jems.append(tmp_d.pop())
        for i in range(b):
            jems.append(tmp_d.popleft())
        jems.sort()
        for i in range(min(len(jems), k - b - a)):
            if jems[i] < 0:
                jems[i] = 0
            else:
                break
        tmp_score = sum(jems)
        if tmp_score > score:
            score = tmp_score
print(score)
