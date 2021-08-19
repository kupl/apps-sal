import sys

# inf = open('input.txt', 'r')
# reader = (line.rstrip() for line in inf)
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

t = int(input())
for _ in range(t):
    n = int(input())
    pack = []
    for i in range(n):
        xi, yi = list(map(int, input().split()))
        pack.append((xi, yi))
    pack.sort()
    x_prev, y_prev = 0, 0
    ans = []
    for x, y in pack:
        if y < y_prev:
            print('NO')
            break
        ans.append('R' * (x - x_prev) + 'U' * (y - y_prev))
        x_prev, y_prev = x, y
    else:
        print('YES')
        print(''.join(ans))

# inf.close()
