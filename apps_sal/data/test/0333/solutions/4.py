from sys import stdin, stdout

f = stdin.readline().strip()
s = stdin.readline().strip()

if f == s:
    stdout.write('-1')
else:
    stdout.write(str(max(len(s), len(f))))
