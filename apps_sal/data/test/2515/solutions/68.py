import math
Q = int(input())
lr = []
for _ in range(Q):
    (l, r) = map(int, input().split())
    lr.append((l, r))
Primes = [1] * (10 ** 5 + 1)
(Primes[0], Primes[1]) = (0, 0)
for i in range(2, 10 ** 5 + 1):
    if Primes[i] == 0:
        continue
    M = int(math.sqrt(i)) + 1
    for j in range(2, M):
        if i % j == 0:
            Primes[i] = 0
            break
    else:
        for k in range(i * 2, 10 ** 5 + 1, i):
            Primes[k] = 0
like2017 = [0] * (10 ** 5 + 1)
for x in range(10 ** 5 + 1):
    if Primes[x] == 1 and Primes[(x + 1) // 2] == 1:
        like2017[x] = 1
s = [0] * (len(like2017) + 1)
for a in range(len(like2017)):
    s[a + 1] = s[a] + like2017[a]
for (l, r) in lr:
    ans = s[r + 1] - s[l]
    print(ans)
