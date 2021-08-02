import math
Q = int(input())
MAX = 10**5
lim = int(math.sqrt(MAX))
primes = [2]
table = [i + 1 for i in range(2, MAX, 2)]
while lim > table[0]:
    primes.append(table[0])
    table = [j for j in table if j % table[0] != 0]
primes = set(primes + table)

ans = [0] * (MAX + 1)
for i in range(3, MAX + 1, 2):
    if i in primes and (i + 1) // 2 in primes:
        ans[i] = 1
for i in range(1, MAX + 1):
    ans[i] = ans[i] + ans[i - 1]
for _ in range(Q):
    l, r = map(int, input().split())
    print(ans[r] - ans[l - 1])
