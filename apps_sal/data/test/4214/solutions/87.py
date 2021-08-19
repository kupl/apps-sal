import itertools
import math
N = int(input())
x_list = [0] * N
y_list = [0] * N
for i in range(N):
    (x_list[i], y_list[i]) = map(int, input().split())
l_sum = 0
l = 0
for comb in itertools.combinations(range(N), 2):
    l = ((x_list[comb[0]] - x_list[comb[1]]) ** 2 + (y_list[comb[0]] - y_list[comb[1]]) ** 2) ** 0.5
    l_sum += l
ans = 2 * l_sum / N
print(ans)
