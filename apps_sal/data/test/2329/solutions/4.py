import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
s = [set() for i in range(m + 1)]
u = [-1] * (m + 1)
for i in range(n):
    s[a[i]].add(i + 1)


def find(x):
    if u[x] <= 0:
        return x
    else:
        u[x] = find(u[x])
        return u[x]


count = 0
for i in range(n - 1):
    if a[i] != a[i + 1]:
        count += 1
ans = [count]
for i in range(1, m):
    (x, y) = map(int, input().split())
    x = find(x)
    y = find(y)
    if len(s[x]) < len(s[y]):
        (x, y) = (y, x)
    for j in s[y]:
        if j - 1 in s[x]:
            count -= 1
        if j + 1 in s[x]:
            count -= 1
    ans.append(count)
    s[x] |= s[y]
    u[y] = x
for i in ans:
    print(i)
