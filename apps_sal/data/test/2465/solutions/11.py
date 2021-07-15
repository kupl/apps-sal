import sys

T = int(sys.stdin.readline().strip())
for t in range (0, T):
    ang = int(sys.stdin.readline().strip())
    n = 180
    if ang % 2 == 0:
        ang = ang // 2
        n = n // 2
    if ang % 2 == 0:
        ang = ang // 2
        n = n // 2
    if ang % 5 == 0:
        ang = ang // 5
        n = n // 5
    if ang % 3 == 0:
        ang = ang // 3
        n = n // 3
    if ang % 3 == 0:
        ang = ang // 3
        n = n // 3
    if n == ang + 1:
        n = n * 2
        ang = ang * 2
    print(n)
