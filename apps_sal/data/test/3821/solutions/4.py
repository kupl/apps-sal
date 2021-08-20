n = int(input())
l = [float(x) for x in input().split()]
assert len(l) == n
l.sort()
if l[-1] == 1:
    print('%11.10f' % 1)
else:
    sig = 0
    prod = 1
    while sig < 1 and len(l) > 0:
        x = l.pop()
        sig += x / (1 - x)
        prod *= 1 - x
    print('%11.10f' % (sig * prod))
