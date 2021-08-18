import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
edge = [[] for _ in [0] * n]
for i in range(~-n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a] += [[b, i]]
ans = [0] * ~-n


def dfs(now, color):
    count = 1
    for to, i in edge[now]:
        if count == color:
            count += 1
        ans[i] = count
        dfs(to, count)
        count += 1


dfs(0, 0)

print(max(ans))
for p in ans:
    print(p)
