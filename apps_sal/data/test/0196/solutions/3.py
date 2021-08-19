from sys import stdin
line = stdin.readline().rstrip().split()
x = int(line[0])
k = int(line[1])
if x == 0:
    print(0)
else:
    nn = pow(2, k, 1000000007)
    result = (nn * 2 * x - nn + 1) % 1000000007
    print(result)
