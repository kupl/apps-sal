from sys import stdin, stdout, exit
(n, m) = list(map(int, stdin.readline().split()))
cts = [[0] * 5 for i in range(m)]
for i in range(n):
    s = stdin.readline().strip()
    for (j, c) in enumerate(s):
        cts[j][ord(c) - ord('A')] += 1
a = list(map(int, stdin.readline().split()))
ans = 0
for j in range(m):
    ans += max(cts[j]) * a[j]
stdout.write(str(ans) + '\n')
