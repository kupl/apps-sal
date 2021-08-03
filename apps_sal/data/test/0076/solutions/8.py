from sys import stdin, stdout


n, m, a, b = map(int, stdin.readline().split())
ans = float('inf')

if not n % m:
    stdout.write('0')
else:
    mod = n % m
    ans = min(ans, mod * b)
    ans = min(ans, (m - mod) * a)

    stdout.write(str(ans))
