from sys import stdin, stdout

n, k = list(map(int, stdin.readline().split()))
values = list(map(int, stdin.readline().split()))
cnt = 0
sweet = 0

for i in range(n):
    cnt += values[i]

    v = min(min(cnt, 8), k - sweet)
    sweet += v
    cnt -= v

    if sweet == k:
        stdout.write(str(i + 1))
        break
else:
    stdout.write('-1')
