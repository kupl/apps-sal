from sys import stdin, stdout
n, k = map(int, stdin.readline().split())
no = list(map(int, stdin.readline().split()))
yes = list(map(int, stdin.readline().split()))
mn = float('inf')
for i in range(n):
    mn = min(mn, yes[i] // no[i])
cnt = mn
while k > 0:
    for i in range(n):
        if yes[i] // no[i] == mn:
            k -= no[i] * (mn + 1) - yes[i]
            yes[i] = no[i] * (mn + 1)
    if k >= 0:
        cnt += 1
        mn += 1
stdout.write(str(cnt))
