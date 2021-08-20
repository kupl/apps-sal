import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    s = sys.stdin.readline().strip()
    (x, y, z) = (s.count('R'), s.count('S'), s.count('P'))
    if max(x, y, z) == x:
        print('P' * len(s))
    elif max(x, y, z) == y:
        print('R' * len(s))
    else:
        print('S' * len(s))
