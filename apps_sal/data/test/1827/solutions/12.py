from collections import deque
n = int(input())
h = sorted(list(map(int, input().split())))
data = deque(h)
for i in range(n):
    print(data[0], data[-1])
    data.pop()
    data.popleft()
