import sys
N = int(input())
a = list(map(int, input().split()))
sys.setrecursionlimit(1500)


def solve(n, slope, d, slope2=None, d2=0, point=None):
    if n == N:
        if point is None:
            return False
        else:
            return True
    if a[n] == slope * n + d:
        return solve(n + 1, slope, d, slope2, d2, point)
    elif point is None:
        return solve(n + 1, slope, d, slope2, d2, point=n)
    else:
        slope2 = (a[n] - a[point]) / (n - point)
        if slope2 != slope:
            return False
        d2 = a[point] - point * slope2
        return solve(n + 1, slope, d, slope2, d2, point)


for (i, j) in [(0, 1), (1, 2), (0, 2)]:
    slope = (a[j] - a[i]) / (j - i)
    d = a[i] - i * slope
    if solve(0, slope, d):
        print('Yes')
        break
else:
    print('No')
