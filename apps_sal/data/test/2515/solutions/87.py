import math
from itertools import accumulate
Q = int(input())
lr = [list(map(int, input().split())) for _ in range(Q)]
MAX = 10 ** 5
lim = int(math.sqrt(MAX))
primes = [2]
table = [i + 1 for i in range(2, MAX, 2)]
while lim > table[0]:
    primes.append(table[0])
    table = [j for j in table if j % table[0] != 0]
primes = set(primes + table)
similars = [0] * MAX
for i in range(2, MAX):
    if i in primes and (i + 1) // 2 in primes:
        similars[i] = 1
similars = list(accumulate(similars))
for i in lr:
    (l, r) = i
    print(similars[r] - similars[l - 1])
