from heapq import *


def main():
    def find(x):
        parent = data[x]
        if parent < 0:
            return x
        root = find(parent)
        data[x] = root
        return root

    def union(x, y):
        root, second = find(x), find(y)
        if root == second:
            return False
        if height[root] < data[second]:
            second, root = root, second
        data[root] += data[second]
        height[root] = max(height[root], height[second] + 1)
        data[second] = root
        return True

    N = int(input())
    X = [(0, 0)] * N
    Y = [(0, 0)] * N

    for i in range(N):
        x, y = list(map(int, input().split()))
        X[i] = (x, i)
        Y[i] = (y, i)

    X.sort()
    Y.sort()
    H = []

    for i in range(N - 1):
        x1, j1 = X[i]
        x2, j2 = X[i + 1]
        y1, k1 = Y[i]
        y2, k2 = Y[i + 1]
        heappush(H, (x2 - x1, j1, j2))
        heappush(H, (y2 - y1, k1, k2))

    answer = 0
    data = [-1] * (N + 1)
    height = [0] * (N + 1)

    while H:
        w, s, t = heappop(H)
        if union(s, t):
            answer += w

    print(answer)


def __starting_point():
    main()


__starting_point()
