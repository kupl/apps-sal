(n, q) = list(map(int, input().split()))
officers = list(map(int, input().split()))
s = [[] for _ in range(n)]
c = [1] * n
b = [0] * n
for (i, v) in enumerate(officers):
    s[v - 1].append(i + 1)
traversal = []


def dfs():
    stack = [0]
    while stack:
        n = stack.pop()
        traversal.append(n)
        for child in reversed(s[n]):
            stack.append(child)


dfs()
for i in range(n):
    b[traversal[i]] = i
for i in range(n - 1, -1, -1):
    for child in s[i]:
        c[i] += c[child]
answer = []
for _ in range(q):
    (u, k) = list(map(int, input().split()))
    start = b[u - 1]
    if k <= c[u - 1]:
        answer.append(str(traversal[start + k - 1] + 1))
    else:
        answer.append('-1')
print('\n'.join(answer))
