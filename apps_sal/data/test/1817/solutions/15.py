from collections import deque
n = int(input())
x = [*map(int, input().split())]
xx = deque()
x.sort()
for i in x:
    xx.append(i)
turn = 0
while len(xx) > 1:
    if turn % 2 == 0:
        xx.pop()
    else:
        xx.popleft()
    turn += 1
print(xx.pop())
