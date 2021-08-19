import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
a = sorted(map(int, input().split()))
for q in map(int, input().split()):
    if q >= a[-1]:
        print(n, end=' ')
    else:
        low = 0
        high = n
        while high - low:
            t = (low + high) // 2
            if q >= a[t]:
                low = t + 1
            else:
                high = t
        print(low, end=' ')
