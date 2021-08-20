from sys import stdin, stdout
n = int(stdin.readline())
ans = 0
for i in range(1, n):
    if not (n - i) % i:
        ans += 1
stdout.write(str(ans))
