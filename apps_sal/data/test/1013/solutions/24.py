from sys import stdin, stdout
(n, m) = map(int, stdin.readline().split())
ans = 4
for i in range(1, n + 1):
    ind = 1
    for v in list(map(int, stdin.readline().split())):
        if v and (ind == 1 or ind == m or i == 1 or (i == n)):
            ans = 2
        ind += 1
stdout.write(str(ans))
