from sys import stdin, stdout
(n, k, t) = list(map(int, stdin.readline().rstrip().split()))
print(max([min([n, t]) - max([0, t - k]), 0]))
