from collections import deque
N = int(input())
T = ('3', '5', '7')
que = deque(list(T))
ans = 0
while que:
    num = que.popleft()
    if int(num) > N:
        continue
    if len(set(num)) == 3:
        ans += 1
    for t in T:
        que.append(num + t)
print(ans)
