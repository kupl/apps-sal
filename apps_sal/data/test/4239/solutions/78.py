from collections import deque
n = int(input())
table = [-1] * 100001
table[0] = 0
d = deque()
d.append(0)
can = []
can.append(1)
for i in range(1, 50):
    if 6**i <= 100000:
        can.append(6**i)
    else:
        break
    if 9**i <= 100000:
        can.append(9**i)
while d:
    w = d.popleft()
    for i in can:
        if w + i > 100000:
            continue
        if not table[w + i] == -1:
            continue
        table[w + i] = table[w] + 1
        d.append(w + i)
print(table[n])
