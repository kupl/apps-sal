import sys
n = int(sys.stdin.readline().replace('\n', ''))
a = [int(x) for x in sys.stdin.readline().replace('\n', '').split(' ')]
ok = True
for (day, teams) in enumerate(a):
    if teams < 0:
        sys.stdout.write('NO')
        ok = False
        break
    elif teams % 2 == 0:
        pass
    elif day + 1 < len(a):
        a[day + 1] -= 1
    else:
        sys.stdout.write('NO')
        ok = False
        break
if ok:
    sys.stdout.write('YES')
