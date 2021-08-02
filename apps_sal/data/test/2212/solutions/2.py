import sys
n = int(input())
o = 1
e = 2
for i in range(n):
    for j in range(n):
        if abs(i - n // 2) + abs(j - n // 2) <= n // 2:
            sys.stdout.write(str(o))
            o += 2
        else:
            sys.stdout.write(str(e))
            e += 2
        sys.stdout.write(' ')
    sys.stdout.write('\n')
