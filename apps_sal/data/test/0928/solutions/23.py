from collections import deque

N, K = [int(i) for i in input().split()]
AS = [int(i) for i in input().split()]

l = deque()
s = 0
cnt = 0

s = 0
for i in range(N):
    a = AS[i]
    s += a
    l.append(a)
    if s >= K:
        cnt += N - i
        while s - l[0] >= K:
            s -= l[0]
            cnt += N - i
            l.popleft()
        s -= l[0]
        l.popleft()


print(cnt)
