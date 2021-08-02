import math
n = int(input())
ans = [x + 1 for x in range(n.bit_length(), -1, -1) if (n >> x) & 1]
for x in ans:
    print(x, end=' ')
