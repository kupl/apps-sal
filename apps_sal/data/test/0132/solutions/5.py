from collections import deque

n = int(input())
a = deque(map(int, input().split()))
ps = [0] * n
mindif = 2e9
for i in range(n):
    for i in range(n):
        ps[i] = ps[i - 1] if i > 0 else 0
        ps[i] += a[i]
    for i in range(n):
        mindif = min(mindif, abs((ps[i - 1] if i > 0 else 0) - (ps[n - 1] - (ps[i - 1] if i > 0 else 0))))
    a.append(a.popleft())

print(mindif)
