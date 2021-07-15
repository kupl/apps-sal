import sys
l = list(map(int, sys.stdin.readline().rstrip().split()))
cur = 1
t = 0
while True:
    if l[t] < cur:
        if t:
            sys.stdout.write('Valera')
            break
        else:
            sys.stdout.write('Vladik')
            break
    else:
        l[t] -= cur
        cur += 1
        if t:
            t = 0
        else:
            t += 1
