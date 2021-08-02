from collections import deque


def permutation(n, k):
    s = 1
    for _ in range(k):
        s *= n
        s %= mod
        n -= 1
    return s


def bfs():
    nonlocal ans
    q = deque()
    q.append([1, 0])
    visit[1] = 1
    while q:
        x, y = q.popleft()
        a = 0
        for i in T[x]:
            if visit[i] == 0:
                q.append([i, 1])
                visit[i] = 1
                a += 1
        b = k - y - 1
        if b - a < 0:
            print(0)
            return
        ans *= permutation(b, a)
        ans %= mod
    return


n, k = map(int, input().split())
T = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
mod = pow(10, 9) + 7
for _ in range(n - 1):
    a, b = map(int, input().split())
    T[a].append(b)
    T[b].append(a)
ans = k
bfs()
print(ans)
