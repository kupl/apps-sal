import sys
f = sys.stdin
#f = open('H:\\Portable Python 3.2.5.1\\test_248B1.txt')
s = 0
a = [int(u) for u in f.readline().strip().split()]

s = sum(a)

if s % 5 == 0 and s > 0:
    print(s // 5)
else:
    print(-1)
