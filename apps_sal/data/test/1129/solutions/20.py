import sys

INF = 10 ** 9 + 3

fin = sys.stdin
fout = sys.stdout
n = int(fin.readline())
points = list(map(int, fin.readline().split()))
points.sort()
if (n % 2 == 1):
    fout.write(str(points[n // 2]))
else:
    fout.write(str(points[n // 2 - 1]))
