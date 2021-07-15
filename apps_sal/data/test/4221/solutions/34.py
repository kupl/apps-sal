from sys import stdin
s = stdin.readline().rstrip()
if s[-1] == 's':
    print((s + 'es'))
else:
    print((s + 's'))

