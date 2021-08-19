from itertools import permutations
import math
N = int(input())
s = [list(map(int, input().split())) for i in range(N)]


def length(x, y, x1, y1):
    return math.sqrt((x - x1) ** 2 + (y - y1) ** 2)


l = permutations(s)
ans = 0
for i in l:
    for j in range(1, N):
        ans += length(i[j - 1][0], i[j - 1][1], i[j][0], i[j][1])
print(ans / math.factorial(N))
