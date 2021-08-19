import sys
import heapq as hp
#sys.stdin = open('in', 'r')
t = int(sys.stdin.readline())
for ti in range(t):
    n = int(sys.stdin.readline())
    a = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]
    a.sort(key=lambda x: (x[0], -x[1]))
    c = 0
    h = []
    res = 0
    for i in range(n - 1, -1, -1):
        hp.heappush(h, a[i][1])
        while c + i < a[i][0]:
            res += hp.heappop(h)
            c += 1
    print(res)


# sys.stdout.write('YES\n')
# sys.stdout.write(f'{res}\n')
#sys.stdout.write(f'{y1} {x1} {y2} {x2}\n')
