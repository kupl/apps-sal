n = int(input())
dx = [0 for i in range(n + 1)]
dy = [0 for i in range(n + 1)]
for i, ch in enumerate(input()):
    dx[i + 1] = dx[i]
    dy[i + 1] = dy[i]
    if ch == 'U':
        dy[i + 1] += 1
    elif ch == 'D':
        dy[i + 1] -= 1
    elif ch == 'R':
        dx[i + 1] += 1
    else:
        assert ch == 'L'
        dx[i + 1] -= 1
x, y = list(map(int, input().split()))
def canChange(left, right):
    dx1 = dx[left]
    dy1 = dy[left]
    dx3 = dx[-1] - dx[right]
    dy3 = dy[-1] - dy[right]
    dx2 = x - dx1 - dx3
    dy2 = y - dy1 - dy3
    length = right - left
    free = length - (abs(dx2) + abs(dy2))
    return free >= 0 and free % 2 == 0
result = n + 1
ptr = n + 1
for i in reversed(list(range(n))):
    while ptr - 1 >= i and canChange(i, ptr - 1):
        ptr -= 1
        result = min(result, ptr - i)
if ptr == n + 1:
    print(-1)
else:
    print(result)

