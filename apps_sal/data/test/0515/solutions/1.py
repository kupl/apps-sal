from sys import stdin, stdout

k = int(stdin.readline())
if k > 36:
    stdout.write('-1')
else:
    ans = '8' * (k // 2)

    if k & 1:
        ans += '6'

    stdout.write(ans)
