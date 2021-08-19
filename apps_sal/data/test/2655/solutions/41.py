from collections import deque
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
q = deque([a[0]])
ans = 0
for i in range(n - 1):
    ans += q.popleft()
    q.extend([a[i + 1], a[i + 1]])
print(ans)
