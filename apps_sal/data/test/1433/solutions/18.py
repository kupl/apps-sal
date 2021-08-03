n, m = list(map(int, input().split()))
a, b = [], [[] for i in range(m)]

for i in range(n):
    a += [list(map(int, input().split()))]
    for j in range(m):
        b[j] += [a[i][j]]


def count(arr):
    l, r = -1, -1
    for i in range(len(arr)):
        if arr[i] == 1:
            l = i
            break
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 1:
            r = i
            break
    if l == -1:
        return 0
    return l + (len(arr) - r - 1) + 2 * (sum(arr[i] == 0 for i in range(l + 1, r)))


print(sum(count(a[i]) for i in range(n)) + sum(count(b[j]) for j in range(m)))
