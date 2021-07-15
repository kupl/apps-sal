from collections import deque
n, k = list(map(int, input().split()))
s = input()
que = deque()
que.append(s)
d = {}
num = 0
cost = 0
while que:
    q = que.popleft()
    if q not in d:
        cost += n - len(q)
        num += 1
        if num == k:
            print(cost)
            return
        d[q] = 1
        for j in range(len(q)):
            t = q[:j] + q[j + 1:]
            if t not in d:
                que.append(t)

print(-1)


