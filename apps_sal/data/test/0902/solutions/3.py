from collections import deque

n, k = list(map(int, input().split()))
a = deque(list(map(int, input().split())))
f = a.popleft()
s = a.popleft()
cnt = 0
while cnt < k:
    if f > s:
        cnt += 1
        a.append(s)
        s = a.popleft()
    else:
        cnt = 1
        a.append(f)
        f, s = s, a.popleft()
    if f == n:
        cnt = k
print(f)

