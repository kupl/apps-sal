import itertools
import math

N = int(input())
L = [list(map(int, input().split())) for n in range(N)]
I = list(itertools.permutations(L))
sum = 0

for i in I:
    for n in range(N - 1):
        sum += math.sqrt((i[n + 1][0] - i[n][0])**2 + (i[n + 1][1] - i[n][1])**2)

print(sum / len(I))
