import sys

# inf = open('input.txt', 'r')
# reader = (line.rstrip() for line in inf)
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ctr = 0
    sm = sum(a)
    for val in a:
        if val == 0:
            ctr += 1
    if sm + ctr == 0:
        ctr += 1
    print(ctr)

# inf.close()
