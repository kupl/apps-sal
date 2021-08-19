n = int(input())
shortcuts = input().split()
for i in range(n):
    shortcuts[i] = int(shortcuts[i]) - 1
mincosts = []
for i in range(n):
    mincosts.append(i)
for i in range(n - 1):
    a = shortcuts[i]
    mincosts[a] = min(mincosts[a], mincosts[i] + 1)
    if i + 1 < n and shortcuts[i] < shortcuts[i + 1]:
        b = a + 1
        while b <= shortcuts[i + 1] and mincosts[b - 1] + 1 < mincosts[b]:
            mincosts[b] = mincosts[b - 1] + 1
            b += 1
        b = a - 1
        while b > i and mincosts[b + 1] + 1 < mincosts[b]:
            mincosts[b] = mincosts[b + 1] + 1
            b -= 1
for i in range(1, n):
    mincosts[i] = min(mincosts[i], mincosts[i - 1] + 1)
for i in range(n - 2, -1, -1):
    mincosts[i] = min(mincosts[i], mincosts[i + 1] + 1)
for i in range(n):
    mincosts[i] = str(mincosts[i])
print(' '.join(mincosts))
