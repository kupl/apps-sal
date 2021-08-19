import sys

n = int(sys.stdin.readline())
things = list(map(int, sys.stdin.readline().split()))

#maxnum = max(things)
lastnum = 1
count = [0] * (n + 1)
for num in things:
    if num <= n:
        count[num] = 1

for num in things:
    if num > n or count[num] > 1:
        while count[lastnum]:
            lastnum += 1
        count[lastnum] = 1
        sys.stdout.write(str(lastnum) + ' ')
    else:
        count[num] = 2
        sys.stdout.write(str(num) + ' ')
