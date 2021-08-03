from sys import stdin, stdout

c, v0, v1, a, l = map(int, stdin.readline().split())
cnt = 0
ans = 0

while cnt < c:
    cnt += v0
    v0 = min(v0 + a, v1)
    ans += 1

    if cnt >= c:
        break

    cnt -= l


stdout.write(str(ans))
