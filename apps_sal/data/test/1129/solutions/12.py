from sys import stdin
n = int(stdin.readline())
points = sorted((int(x) for x in stdin.readline().split()))
if n % 2 == 0:
    print(points[n // 2 - 1])
else:
    print(points[n // 2])
