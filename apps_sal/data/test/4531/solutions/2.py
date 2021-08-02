import sys
from collections import deque
from types import GeneratorType
sys.setrecursionlimit(200000)
input = sys.stdin.readline


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


n = int(input())
val = [int(i) for i in input().split()]
tree = [[] for i in range(n + 1)]
dp = [0 for i in range(n + 1)]
s = [0 for i in range(n + 1)]
ans = [0 for i in range(n + 1)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)


@bootstrap
def dfs1(node, dist, pd):

    for child in tree[node]:
        if child == pd:
            continue
        yield dfs1(child, dist + 1, node)
        dp[node] += dp[child]
        s[node] += s[child]
    dp[node] += val[node - 1] * dist
    s[node] += val[node - 1]
    yield dp[node]


dfs1(1, 0, 1)
q = deque()
ans[1] = dp[1]
for node in tree[1]:
    q.append((node, 1))

while len(q) > 0:
    node, pd = q.popleft()
    sub_dp = ans[pd] - (dp[node] + s[node])
    added = s[1] - s[node]
    ans[node] = sub_dp + added + dp[node]
    for child in tree[node]:
        if child == pd:
            continue
        q.append((child, node))
print(max(ans))
