from sys import stdin, stdout
n, k = map(int, stdin.readline().split())

cnt = k - 8
if (n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12):
    cnt += 31
elif n == 2:
    cnt += 28
else:
    cnt += 30

if cnt % 7:
    ans = 2 + cnt // 7
else:
    ans = 1 + cnt // 7

stdout.write(str(ans))
