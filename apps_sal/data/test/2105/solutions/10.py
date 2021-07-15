import sys

[n, m] = list(map(int, sys.stdin.readline().strip().split(' ')))
s = list(sys.stdin.readline().strip().split(' '))
t = list(sys.stdin.readline().strip().split(' '))
q = int(sys.stdin.readline().strip())
for i in range(q):
    year = int(sys.stdin.readline())
    print(s[(year-1) % n] + t[(year-1) % m])
