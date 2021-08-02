from collections import defaultdict
n = int(input())
d = defaultdict(set)
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    d[a].add(b)
    d[b].add(a)

a = list(map(int, input().split()))


def solve(a):
    if a[0] != 1:
        return 'No'
    i, j = 1, 0
    while i < n and j < n:
        if a[j] in d[a[i]]:
            i += 1
        else:
            j += 1
    if j == n and i != n:
        return 'No'
    return 'Yes'


print(solve(a))
