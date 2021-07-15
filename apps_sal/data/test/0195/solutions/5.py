from sys import stdin, stdout

a, b, c, d = map(int, stdin.readline().split())
q = d - a - b + c

if c > min(a, b) or q <= 0:
    stdout.write('-1')
else:
    stdout.write(str(q))
