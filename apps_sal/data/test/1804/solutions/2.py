import sys
input = sys.stdin.readline
(N, M) = input().split()
(a, b, c, d) = [int(10000000000.0) for _ in range(4)]
for i in range(int(input())):
    (x, y) = list(map(int, input().split()))
    (a, b, c, d) = (min(a, x + y), min(b, x - y), min(c, -x + y), min(d, -x - y))
(res, pos) = (int(10000000000.0), 0)
for i in range(int(input())):
    (x, y) = list(map(int, input().split()))
    ans = max(max(x + y - a, x - y - b), max(-x + y - c, -x - y - d))
    if ans < res:
        pos = i + 1
        res = ans
print(res, pos, sep='\n')
