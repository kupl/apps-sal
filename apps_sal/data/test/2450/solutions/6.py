import sys
input = sys.stdin.readline
for f in range(int(input())):
    (n, m, x, y) = map(int, input().split())
    y = min(y, 2 * x)
    cost = 0
    for i in range(n):
        r = input()
        white = False
        for j in range(m):
            if r[j] == '.':
                if white:
                    cost += y
                    cost -= x
                    white = False
                else:
                    cost += x
                    white = True
            else:
                white = False
    print(cost)
