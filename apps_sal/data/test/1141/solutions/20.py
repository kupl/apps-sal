import sys

sys.setrecursionlimit(100000000)


N, M = map(int, input().split())
line = [x for x in input()]
for t in range(M):
    l, r, c1, c2 = map(str, input().split())
    l = int(l)
    r = int(r)
    for i in range(l - 1, r):
        if line[i] == c1:
            line[i] = c2

print(''.join(line), flush=True)
