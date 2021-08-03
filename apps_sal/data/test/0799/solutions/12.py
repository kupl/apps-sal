from sys import stdin, stdout
n = int(stdin.readline())
values = list(map(int, stdin.readline().split()))
mx = max(values)

cnt = 0
for i in range(n):
    cnt += mx - values[i]

stdout.write(str(cnt))
