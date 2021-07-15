from collections import deque

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

q = deque()
q.append(a[0])
ans = 0
for i in range(1, n):
    b = q.popleft()
    ans += b
    b = min(b, a[i])
    for _ in range(2):
        q.append(b)
print(ans)
