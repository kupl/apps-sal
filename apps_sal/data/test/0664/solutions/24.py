import sys

n = int(sys.stdin.readline())

ok = True
inc = True
last, res, i = 0, 0, 0
first = 0

for num in sys.stdin.readline().split():
    num = int(num)
    if first == 0:
        first = num

    if last > num:
        if inc:
            inc = False
            res = n - i
        else:
            ok = False
    last = num
    i = i + 1

if last > first:
    if inc:
        pass
    else:
        ok = False

if ok:
    print(res)
else:
    print(-1)
