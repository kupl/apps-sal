from collections import deque

S = input()

d = deque()
cnt = 0
for s in S:
    if d:
        if d[-1] != s:
            d.pop()
            cnt += 2
        else:
            d.append(s)
    else:
        d.append(s)

print(cnt)
