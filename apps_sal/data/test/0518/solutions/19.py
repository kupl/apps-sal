import sys
import math
line = sys.stdin.readline().split(' ')
(n, r) = (int(line[0]), int(line[1]))
ans = r * math.sin(math.pi / n) / (1 - math.sin(math.pi / n))
print(ans)
