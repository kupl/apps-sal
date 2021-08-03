import itertools
import math

N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]
Cases = itertools.permutations([x for x in range(N)])

ans = 0
for case in Cases:
    for i in range(N - 1):
        x, y = list(map(int, pos[case[i]]))
        nx, ny = list(map(int, pos[case[i + 1]]))
        tmp = math.sqrt((nx - x)**2 + (ny - y)**2)
        ans += tmp
ans /= math.factorial(N)
print(ans)
