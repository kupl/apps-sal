from collections import deque
n = int(input())
a = list(map(int, input().split()))

ans = deque()
if n % 2 == 0:
    for i in range(n):
        if i % 2 == 1:
            ans.appendleft(a[i])
        else:
            ans.append(a[i])
else:
    for i in range(n):
        if i % 2 == 0:
            ans.appendleft(a[i])
        else:
            ans.append(a[i])

ans = list(ans)
print((*ans))
