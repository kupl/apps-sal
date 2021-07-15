from sys import stdin, stdout

n = int(stdin.readline())
values = sorted(list(map(int, stdin.readline().split())))

l, r = -1, n
while r - l > 1:
    m = (l + r) >> 1
    
    if (sum(values[m:]) + 5 * m) * 10 >= 45 * n:
        r = m
    else:
        l = m

stdout.write(str(r))
