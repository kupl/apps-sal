def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


(n, d) = mi()
a = li()
a.sort()
ans = set()
for i in range(n):
    x = a[i] - d
    y = a[i] + d
    if i == 0 or a[i - 1] <= x - d:
        ans.add(x)
    if i == n - 1 or y + d <= a[i + 1]:
        ans.add(y)
print(len(ans))
