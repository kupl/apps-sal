from sys import stdin, stdout
(e, n) = map(int, stdin.readline().split())
cnt = 0
ans = 0
for i in range(n):
    s = stdin.readline().rstrip()
    if s.count('1') != e:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)
stdout.write(str(ans))
