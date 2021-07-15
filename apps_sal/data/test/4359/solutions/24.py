import sys
a = list(sys.stdin.read().split())
t = list(zip(*[[int(n[:-1] or 0), int(n[-1])] for n in a]))
print((sum(t[0]) + len((u := sorted(filter(lambda n: n > 0, t[1])))[:0:-1])) * 10 + (u and u[0] or 0))
