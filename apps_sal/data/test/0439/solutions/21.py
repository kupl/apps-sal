from sys import stdin, stdout
n = int(stdin.readline())
m = int(stdin.readline())
if n >= 100:
    stdout.write(str(m))
else:
    stdout.write(str(m % 2 ** n))
