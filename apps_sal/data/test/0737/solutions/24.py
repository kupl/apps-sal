from sys import stdin, stdout

n = int(stdin.readline())

l, r = 0, n + 1
while r - l > 1:
    m = (r + l) >> 1

    if m * m > n:
        r = m
    else:
        l = m

if n > 1:
    ans = 8 + (l - 2) * 4
else:
    ans = 4

n -= l * l
for i in range(l):
    if not i:
        if n:
            ans += 2
            n -= 1
    else:
        if n:
            n -= 1

for i in range(l):
    if not i:
        if n:
            ans += 2
            n -= 1
    else:
        if n:
            n -= 1

stdout.write(str(ans))
