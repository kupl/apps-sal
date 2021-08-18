from collections import deque
N = int(input())
txy = [map(int, input().split()) for _ in range(N)]
t, x, y = [list(i) for i in zip(*txy)]
t = deque(t)
x = deque(x)
y = deque(y)
t.appendleft(0)
x.appendleft(0)
y.appendleft(0)
for i in range(N):
    direct = t[i + 1] - t[i] - abs(x[i + 1] - x[i]) - abs(y[i + 1] - y[i])
    if direct < 0 or direct % 2 != 0:
        print("No")
        return
print("Yes")
