from collections import deque
n = int(input())
a = list(map(int, input().split()))
ans = deque()
check = n % 2
for i in range(len(a)):
    if (i + check) % 2 == 0:
        ans.append(a[i])
    else:
        ans.appendleft(a[i])
print(*ans)
