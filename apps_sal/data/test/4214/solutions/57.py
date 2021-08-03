from sys import stdin
import math
import itertools

n = int(stdin.readline().rstrip())
x = [0] * n
y = [0] * n
v = [0] * n

for i in range(n):
    x[i], y[i] = [int(x) for x in stdin.readline().rstrip().split()]
    v[i] = i

cnt = 0
ans = 0
for idx in list(itertools.permutations(v)):
    # print(idx)

    cnt += 1
    for i in range(1, n):
        ans += math.sqrt((x[idx[i]] - x[idx[i - 1]]) * (x[idx[i]] - x[idx[i - 1]]) + (y[idx[i]] - y[idx[i - 1]]) * (y[idx[i]] - y[idx[i - 1]]))

print((ans / cnt))
