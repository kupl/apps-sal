from sys import stdin, stdout, exit
import math
(n, k) = list(map(int, stdin.readline().split()))
ans = round((-3 + math.sqrt(9 + 8 * (k + n))) / 2)
stdout.write(str(n - ans) + '\n')
