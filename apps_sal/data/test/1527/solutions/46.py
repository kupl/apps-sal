from collections import deque
import _pickle as cPickle
import cProfile
h, w = map(int, input().split())
s = [["#"] * (w + 2)] + [["#"] + list(input()) + ["#"] for i in range(h)] + [["#"] * (w + 2)]
ans = 0
A = list()
for i in range(1, h + 1):
    for j in range(1, w + 1):
        t = cPickle.loads(cPickle.dumps(s, -1))
        c = dict()
        A = list()
        if s[i][j] == "#":
            continue
        a = deque([[i, j, 0]])
        while len(a) > 0:
            x, y, cnt = a.popleft()
            t[x][y] = "#"
            if t[x - 1][y] == ".":
                if [x - 1, y, cnt + 1] not in A:
                    a.append([x - 1, y, cnt + 1])
                    A.append([x - 1, y, cnt + 1])
            if t[x + 1][y] == ".":
                if [x + 1, y, cnt + 1] not in A:
                    a.append([x + 1, y, cnt + 1])
                    A.append([x + 1, y, cnt + 1])
            if t[x][y - 1] == ".":
                if [x, y - 1, cnt + 1] not in A:
                    a.append([x, y - 1, cnt + 1])
                    A.append([x, y - 1, cnt + 1])
            if t[x][y + 1] == ".":
                if [x, y + 1, cnt + 1] not in A:
                    a.append([x, y + 1, cnt + 1])
                    A.append([x, y + 1, cnt + 1])
        ans = max(ans, cnt)
print(ans)
