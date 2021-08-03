from collections import deque
n = int(input())
num = [[] for _ in range(n)]
for i in range(n - 1):
    a, b, c = list(map(int, input().split()))
    num[a - 1].append([b, c])
    num[b - 1].append([a, c])
q, k = list(map(int, input().split()))
seen = [False] * n
queue = deque()
queue.append(k)
ans = [0] * n
seen[k - 1] = True
for i in range(n):
    if len(queue) == 0:
        break
    num1 = queue.popleft()
    for j in range(len(num[num1 - 1])):
        num2 = num[num1 - 1][j][0]
        if seen[num2 - 1] == False:
            queue.append(num2)
            seen[num2 - 1] = True
            ans[num2 - 1] = ans[num1 - 1] + num[num1 - 1][j][1]
for i in range(q):
    x, y = list(map(int, input().split()))
    print((ans[x - 1] + ans[y - 1]))
