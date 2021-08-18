from collections import deque
N, = list(map(int, input().split()))
X = list(map(int, input().split()))
R = []
A1 = []
A2 = []
ng = 0
for i in range(N - 1, -1, -1):
    j = N - 1 - i + 1
    if X[i] == 1:
        R.append((i + 1, j))
        A1.append((i + 1, j))
    elif X[i] == 2:
        if not A1:
            ng = 1
            break
        x, y = A1.pop()
        R.append((i + 1, y))
        A2.append((i + 1, y))
    elif X[i] == 3:
        if A2:
            x, y = A2.pop()
            R.append((x, j))
            R.append((i + 1, j))
            A2.append((i + 1, j))
        elif A1:
            x, y = A1.pop()
            R.append((x, j))
            R.append((i + 1, j))
            A2.append((i + 1, j))
        else:
            ng = 1
if ng:
    print(-1)
else:
    print(len(R))
    for x, y in R:
        print(N - y + 1, x)
