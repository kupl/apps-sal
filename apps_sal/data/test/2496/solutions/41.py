from math import gcd

N = int(input())
A = list([int(x) for x in input().split()])

max_a = max(A)

before = 0
result = [0 for _ in range(max_a + 1)]

for i in A:
    before = gcd(before, i)
    result[i] += 1

is_pairwise = True

for i in range(2, max_a + 1):
    cnt = 0
    for j in range(i, max_a + 1, i):
        cnt += result[j]
    if cnt > 1:
        is_pairwise = False
        break

if is_pairwise:
    print('pairwise coprime')
    return
if before == 1:
    print('setwise coprime')
else:
    print('not coprime')

