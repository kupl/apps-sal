import bisect
n = int(input())
t = [1, 2, 4, 8, 16, 32, 64]

print(t[bisect.bisect_right(t, n) - 1])
