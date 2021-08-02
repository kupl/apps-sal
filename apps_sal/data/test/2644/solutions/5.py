from collections import deque
import sys

n = int(input())
p = list(map(int, input().split()))

stack = deque([])
memo = [0] * (n - 1)

for i in range(n - 1):
    if p[i] > (i + 1) and p[i + 1] < (i + 2):
        stack.append(i)
        memo[i] = 1

ans = []

while stack:
    i = stack.pop()
    if memo[i] == 2:
        # print('p1')
        print((-1))
        return
    p[i], p[i + 1] = p[i + 1], p[i]
    memo[i] = 2
    ans.append(i + 1)

    if i > 0 and p[i - 1] > i and p[i] < (i + 1) and memo[i - 1] == 0:
        stack.append(i - 1)
        memo[i - 1] = 1

    if i + 2 < n and p[i + 1] > (i + 2) and p[i + 2] < (i + 3) and memo[i + 1] == 0:
        stack.append(i + 1)
        memo[i + 1] = 1

# print(p)
# print(ans)

if len(ans) != n - 1:
    # print('p2')
    print((-1))
    return

f = 1

for i in range(n):
    if p[i] != i + 1:
        f = 0
        break

if f:
    for ansi in ans:
        print(ansi)
else:
    # print('p3')
    print((-1))
