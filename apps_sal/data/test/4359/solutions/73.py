import sys
t = list(zip(*[[int(n[:-1] or 0), int(n[-1])] for n in (list(sys.stdin.read().split()))]))
print((sum(t[0]) + len((u := sorted(filter(lambda n: n > 0, t[1])))[:0:-1])) * 10 + (u and u[0] or 0))
