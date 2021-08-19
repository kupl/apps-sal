import sys

# inf = open('input.txt', 'r')
# reader = (line.rstrip() for line in inf)
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

t = int(input())
for _ in range(t):
    a, b, c, n = list(map(int, input().split()))
    if (a + b + c + n) % 3 == 0:
        each = (a + b + c + n) // 3
        if a <= each and b <= each and c <= each:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

# inf.close()
