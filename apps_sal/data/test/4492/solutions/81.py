import collections
(n, x) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
q = collections.deque()
if a[0] <= x:
    q.append(a[0])
else:
    ans += a[0] - x
    q.append(x)
for i in range(1, n):
    tmp = q[-1] + a[i]
    if tmp <= x:
        q.append(a[i])
    else:
        ans += tmp - x
        q.append(x - q[-1])
    q.popleft()
print(ans)
