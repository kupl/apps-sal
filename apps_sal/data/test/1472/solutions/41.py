from sys import stdin
nii = lambda: map(int, stdin.readline().split())
lnii = lambda: list(map(int, stdin.readline().split()))

n, x, y = nii()
x -= 1
y -= 1
ans = [0 for i in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        dist1 = j - i
        dist2 = abs(i - x) + 1 + abs(j - y)
        dist = min(dist1, dist2)
        ans[dist] += 1

for i in ans[1:]:
    print(i)
