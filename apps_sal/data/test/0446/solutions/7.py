from sys import stdin, stdout

n = int(stdin.readline())
dividers = []
sze = 20

for i in range(1, sze):
    v = ((1 << i) - 1) * (1 << (i - 1))
    dividers.append(v)

for v in dividers[::-1]:
    if not n % v:
        stdout.write(str(v))
        break
