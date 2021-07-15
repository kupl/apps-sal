n = int(input().strip())
x = list(map(int, input().strip().split()))
best = 0
l = 1
r = n

def test(rsize):
    tot = 0
    for i in range(n):
        tot += x[i]
        if i >= rsize:
            tot -= x[i-rsize]
        if tot > 100*rsize:
            return True
    return False

def work():
    for m in range(n, 0, -1):
        if test(m):
            return m
    return 0

print(work())
