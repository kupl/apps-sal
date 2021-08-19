from itertools import permutations
(n, m) = map(int, input().split())
t1 = 1
t2 = 1
while 7 ** t1 < n:
    t1 += 1
while 7 ** t2 < m:
    t2 += 1
count = 0
for perm in permutations(list('0123456'), t1 + t2):
    a = int(''.join(perm[:t1]), 7)
    b = int(''.join(perm[t1:t1 + t2]), 7)
    if a < n and b < m:
        count += 1
print(count)
