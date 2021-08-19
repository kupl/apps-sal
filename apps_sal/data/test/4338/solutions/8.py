from bisect import bisect_right
(n, x, y) = list(map(int, input().split()))
line = sorted(list(map(int, input().split())))
if x > y:
    print(n)
else:
    k = bisect_right(line, x)
    print(k // 2 + k % 2)
