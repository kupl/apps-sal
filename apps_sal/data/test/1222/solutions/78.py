from collections import deque
k = int(input())
ans = []
q = deque([i for i in range(1, 10)])
for i in range(k):
    x = q.popleft()
    ans.append(x)
    if x % 10 != 0:
        q.append(10 * x + (x % 10) - 1)
    q.append(10 * x + (x % 10))
    if x % 10 != 9:
        q.append(10 * x + (x % 10) + 1)

print(ans[k - 1])
