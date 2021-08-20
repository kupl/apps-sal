from collections import deque
(H, W) = (2, 2)
N = 3
ARR = [2, 1, 1]
(H, W) = (3, 5)
N = 5
ARR = [1, 2, 3, 4, 5]
(H, W) = (1, 1)
N = 1
ARR = [1]
(H, W) = list(map(int, input().split()))
N = int(input())
ARR = list(map(int, input().split()))


def calculate(h, w, n, arr):
    resources = deque()
    for (index, ar) in enumerate(arr):
        for m in range(ar):
            resources.append(index + 1)
    nodeStatus = [[False for i in range(w)] for j in range(h)]
    for j in range(h):
        if j % 2 == 0:
            startIndex = 0
            for i in range(startIndex, w, 1):
                nodeStatus[j][i] = str(resources.popleft())
        else:
            startIndex = w - 1
            for i in range(startIndex, -1, -1):
                nodeStatus[j][i] = str(resources.popleft())
    for j in range(h):
        print(' '.join(nodeStatus[j]))


calculate(H, W, N, ARR)
