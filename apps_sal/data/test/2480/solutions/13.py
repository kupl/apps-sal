from collections import deque
(n, k) = map(int, input().split())
a = [int(i) - 1 for i in input().split()]
total = 0
s = [0] * (n + 1)
for i in range(n):
    total += a[i]
    s[i + 1] = total % k
queue = deque()
mp = {}
ans = 0
for j in range(n + 1):
    rem = s[j]
    queue.append(rem)
    if rem in mp:
        ans += mp[rem]
        mp[rem] += 1
    else:
        mp[rem] = 1
    if len(queue) == k:
        mp[queue.popleft()] -= 1
print(ans)
