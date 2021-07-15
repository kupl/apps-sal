import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
for _ in range(M):
    L, R, D = map(int, input().split())
    G[L].append((R, -D))
    G[R].append((L, +D))

ans = [None] * (N + 1)

def calc(i):
    ans[i] = 0
    stack = [i]
    while stack:
        now = stack.pop()
        for next_, d in G[now]:
            if ans[next_] == None:
                ans[next_] = ans[now] + d
                stack.append(next_)
            else:
                if ans[now] + d != ans[next_]:
                    return False
    return True

for i in range(1, N + 1):
    if ans[i] == None:
        if calc(i):
            pass
        else:
            print ('No')
            return


max_ = -10 ** 10
min_ = +10 ** 10
for i in ans[1:]:
    max_ = max(max_, i)
    min_ = min(min_, i)

if max_ - min_ > 10 ** 9:
    print ('No')
else:
    print ('Yes')
