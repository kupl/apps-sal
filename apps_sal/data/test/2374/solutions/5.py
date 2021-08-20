from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
(N, M) = map(int, input().split())
AB = [[0, 0]] + [[int(i) for i in input().split()] for _ in range(N)] + [[1 << 40, 0]]
LR = [[int(i) for i in input().split()] for _ in range(M)]
N += 2
compressed = sorted([a for (a, b) in AB])
bomb = [0] * N
for (a, b) in AB:
    a = bisect_left(compressed, a)
    bomb[a] = b
diff = [bomb[i - 1] ^ bomb[i] for i in range(1, N)]
vec = [[] for _ in range(N)]
convert = {}
for (i, (l, r)) in enumerate(LR):
    if compressed[-1] < l or r < compressed[0]:
        continue
    l = bisect_left(compressed, l) - 1
    r = bisect_right(compressed, r) - 1
    if r <= l:
        continue
    vec[l].append(r)
    vec[r].append(l)
    convert[l, r] = i
visited = [False] * N
parent = [-1] * N
ret = []


def dfs(pre, cur):
    for nex in vec[cur]:
        if nex == pre or visited[nex]:
            continue
        visited[nex] = True
        dfs(cur, nex)
    if pre == -1 and diff[cur] == 1:
        return False
    if diff[cur] == 1:
        diff[cur] ^= 1
        diff[pre] ^= 1
        ret.append(convert[min(pre, cur), max(pre, cur)] + 1)
    return True


for i in range(N - 1):
    if visited[i]:
        continue
    visited[i] = True
    if not dfs(-1, i):
        print(-1)
        break
else:
    ret.sort()
    print(len(ret))
    print(*ret)
