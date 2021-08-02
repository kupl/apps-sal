time = 0
n = int(input())
todo = [] * n

for i in range(n):
    a, b = map(int, input().split())
    todo.append([b, a])

todo.sort()
d = True

for i in range(n):
    time += todo[i][1]
    if todo[i][0] < time:
        d = False
        break

if d:
    print('Yes')
else:
    print('No')
