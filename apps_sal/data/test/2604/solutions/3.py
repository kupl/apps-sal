from sys import stdin, stdout

r, d = list(map(int, stdin.readline().rstrip().split()))
n = int(stdin.readline().rstrip())
crust = 0

for _ in range(n):
    x, y, ri = list(map(int, stdin.readline().rstrip().split()))
    z = (x**2 + y**2)**0.5
    if z - ri >= (r - d) and z + ri <= r:
        crust += 1

print(crust)
