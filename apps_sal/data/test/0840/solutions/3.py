from sys import stdin, stdout
n, k = map(int, stdin.readline().split())
no = list(map(int, stdin.readline().split()))
yes = list(map(int, stdin.readline().split()))
mn = float('inf')
for i in range(n):
    mn = min(mn, yes[i] // no[i])
l = mn
r = mn + k + 1
while r > l + 1:
    m = (l + r) // 2
    cnt = k
    for i in range(n):
        if yes[i] < no[i] * m:
            cnt -= no[i] * m - yes[i]
    if cnt >= 0:
        l = m
    else:
        r = m
stdout.write(str(l))
